import ssl
import time
import binascii
import feedparser
from tqdm import tqdm

from objs.news import News


def conv_to_rss(link):
    if "vk.com" in link:
        group = link[link.find("vk.com") + 7:]
        return "http://feed.exileed.com/vk/feed/%s" % (group + "?count=5")
    return link


class RssParser(object):
    """
    Класс для парсинга RSS-канала.
    Выделяет из общей информации только интереующие нас поля: Заголовок, ссылку, дату публикации.
    """

    def __init__(self, config_links):
        self.links = [conv_to_rss(config_links[i]) for i in config_links]
        self.news = []
        # self.refresh()

    def refresh(self):
        self.news = []
        for link in tqdm(self.links, desc="Getting news"):
            data = 0
            if hasattr(ssl, '_create_unverified_context'):
                ssl._create_default_https_context = ssl._create_unverified_context
                data = feedparser.parse(link)
            self.news += [News(binascii.b2a_base64(data['feed']['title'].replace(' VK feed', '').encode()).decode(),
                               binascii.b2a_base64(entry['link'].encode()).decode(),
                               int(time.mktime(entry['published_parsed']))) for entry in data['entries']]
            time.sleep(1)

    def __repr__(self):
        return "<RSS ('%s','%s')>" % (self.link, len(self.news))
