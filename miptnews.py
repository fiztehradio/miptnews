#!/usr/bin/env python3
#-*- coding: UTF 8 -*-

import os
import sqlite3
from objs.bot import ExportBot, bot_job, echo
from telegram.ext import Updater, MessageHandler, Filters
import logging

database = 'miptnews.db'

if not os.path.isfile(database):
    db = sqlite3.connect(database)
    c = db.cursor()
    c.execute('CREATE TABLE miptnews (id INTEGER PRIMARY KEY, text VARCHAR(200), link VARCHAR(100), date UNIX_TIME, publish UNIX_TIME, chat_id INTEGER, message_id INTEGER)')


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)
bot = ExportBot()
updater = Updater(bot=bot)
dispatcher = updater.dispatcher
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
j = updater.job_queue
j.run_repeating(bot_job, interval=1800, first=0)
updater.start_polling()
