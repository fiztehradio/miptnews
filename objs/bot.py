# -*- coding: UTF 8 -*-
# !/usr/bin/env python3
import configparser
# import socket
import logging
from string import punctuation
from telegram import Bot
import base64
from datetime import datetime

from objs.databasehandler import DatabaseHandler
from objs.rssparser import *
from objs.bitly import Bitly


# socket.setdefaulttimeout(10)


def bot_job(bot, job):
    bot.detect()
    bot.public_posts()


class ExportBot(Bot):
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('./config')
        sources = configparser.ConfigParser()
        sources.read('./sources')
        tokens = configparser.ConfigParser()
        tokens.read('./tokens')
        log_file = config['Export_params']['log_file']
        Bot.__init__(self, token=tokens['Telegram']['access_token'])
        self.pub_pause = int(config['Export_params']['pub_pause'])
        self.delay_between_messages = int(
            config['Export_params']['delay_between_messages'])
        logging.basicConfig(
            format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s',
            level=logging.INFO,
            handlers=[logging.FileHandler(u'%s' % log_file, 'w', 'utf-8')])
        self.db = DatabaseHandler(config['Database']['Path'])
        self.src = RssParser(sources['RSS'])
        self.chat_id = config['Telegram']['chat']
        # self.bot_access_token = tokens['Telegram']['access_token']
        # self.bot = Bot(token=self.bot_access_token)
        self.bit_ly = Bitly(tokens['Bitly']['access_token'])

    def detect(self):
        # получаем 30 последних постов из rss-канала
        self.src.refresh()
        news = self.src.news
        news.reverse()
        # Проверяем на наличие в базе ссылки на новость, если нет, то добавляем в базу данных с
        # отложенной публикацией
        for i in news:
            if not self.db.find_link(i.link):
                now = int(time.mktime(time.localtime()))
                i.publish = now + self.pub_pause
                logging.info(u'Detect news: %s' % str(i))
                if self.db.add_news(i):
                    print('success')

    def public_posts(self):
        now = datetime.now()
        # Получаем 30 последних записей из rss канала и новости из БД, у которых message_id=0
        posts_from_db = self.db.get_post_without_message_id()
        today_news = [i for i in self.src.news if (
            now - datetime.fromtimestamp(i.date)).days < 1]
        # Выбор пересечний этих списков
        for_publishing = list(set(today_news) & set(posts_from_db))
        for_publishing = sorted(for_publishing, key=lambda news: news.date)
        # for_publishing = sorted(today_news, key=lambda news: news.date)
        # Постинг каждого сообщения
        for post in tqdm(for_publishing, desc="Posting news"):
            header = base64.b64decode(post.text).decode('utf8')
            header = ''.join(c for c in header if c not in set(punctuation + '—«»'))
            header = '#' + '_'.join(header.lower().split())
            text = '%s %s' % (header,
                              self.bit_ly.short_link(base64.b64decode(post.link).decode('utf8')))
            a = self.sendMessage(
                chat_id=self.chat_id, text=text)  # , parse_mode=telegram.ParseMode.HTML)
            message_id = a.message_id
            chat_id = a['chat']['id']
            self.db.update(post.link, chat_id, message_id)
            logging.info(u'Public: %s;%s;' %
                         (str(post), message_id))
            time.sleep(self.delay_between_messages)
