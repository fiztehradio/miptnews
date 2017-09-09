import json
import urllib


class Bitly(object):
    def __init__(self, access_token):
        self.access_token = access_token

    def short_link(self, long_link):
        url = 'https://api-ssl.bitly.com/v3/shorten?access_token=%s&longUrl=%s&format=json' \
              % (self.access_token, long_link)
        try:
            return json.loads(urllib.request.urlopen(url).read().decode('utf8'))['data']['url']
        except:
            return long_link
