# coding: utf-8
# Author: lee_zix

import urllib

url_obj = urllib.urlopen('https://mp.weixin.qq.com/s?__biz=MzI2MTIxOTUxMg==&mid=2650368780&idx=3&sn=3e04b9167ac1de7ea5fffc42e0920b42&chksm=f2507edbc527f7cd81a789e56faaf24987012c92290279b9cbeeaa445a33b6300c023a0eaeaf&scene=21#wechat_redirect')
content = url_obj.read()

url_obj.close()