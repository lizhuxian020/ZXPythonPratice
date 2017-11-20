# coding: utf-8
# Author: lee_zix

import utils.file_tools
import urllib


wx_url = 'https://mp.weixin.qq.com/s?__biz=MzI2MTIxOTUxMg==&mid=2650368849&idx=4&sn=1171ca89379842aa6da5fa764434bf43&chksm=f2507e86c527f79055fd4e349a416cd149f5b16c8976b770f5180747c20f698a4d0f03759a29&scene=21#wechat_redirect'
if __name__ == '__main__':
    url_obj = urllib.urlopen('https://www.baidu.com')
    content = url_obj.read()
    print content