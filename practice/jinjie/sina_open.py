# coding: utf-8
# Author: lee_zix

from urllib import urlopen

from weibo import APIClient


APP_KEY = '3914608262'            # app key
APP_SECRET = '3f7c35ffd77bf00b0040c44ccf3edf85'      # app secret
CALLBACK_URL = 'http://baidu.com'  # callback url

client = APIClient(APP_KEY, APP_SECRET, CALLBACK_URL)


r = client.request_access_token('e25b53f6f8c1e6aa0af312ecd5ba15de')
access_token = r.access_token

print client.statuses.user_timeline.get()

print access_token

# url = 'https://api.weibo.com/2/statuses/public_timeline.json?access_token=%s' % access_token
#
#
# url_obj = urlopen('https://api.weibo.com/2/statuses/public_timeline.json')
# print url_obj.read()
