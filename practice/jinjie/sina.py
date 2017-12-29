# coding:utf-8
# Author:lee_zix

from weibo import APIClient
import webbrowser


APP_KEY = '3914608262'            # app key
APP_SECRET = '3f7c35ffd77bf00b0040c44ccf3edf85'      # app secret
CALLBACK_URL = 'http://baidu.com'  # callback url

client = APIClient(APP_KEY, APP_SECRET, CALLBACK_URL)

url = client.get_authorize_url()

webbrowser.open(url)


r = client.request_access_token('e25b53f6f8c1e6aa0af312ecd5ba15de')
access_token = r.access_token

print client.statuses.user_timeline.get()

print access_token
