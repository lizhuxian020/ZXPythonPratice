# coding: utf-8
# Author: lee_zix

import urllib
import os
from utils.file_tools import make_sure_path

url = 'http://op.feiwan.net/manhua/890.html?page=%d' % 2
img_url = 'http://img.feiwan.net/op/manhua/%d/%d.png'

collect = 890

# url_obj = urllib.urlopen("http://www.baiduasd.com")

def load_ji(jishu, dir_path):
    if make_sure_path(dir_path, 'd'):
        for x in range(1, 30):
            a_img_url = img_url % (jishu, x)
            # check404(a_img_url, check404_callback)
            file_name = '%d.png' % x
            full_path = os.path.join(dir_path, file_name)
            try:
                url_obj = urllib.urlopen(a_img_url)
            except Exception, e:
                print e
            else:
                if '404 Not Found' in url_obj.read():
                    print '----end----'
                    return
                url_obj.close()
                print os.system('wget -O %s %s' % (full_path, a_img_url))

        pass



def check404(url, callback):

    try:
        url_obj = urllib.urlopen(url)
    except Exception, e:
        print e
        callback(False)
    else:
        url_obj.close()
        callback(True)

        # print os.system('wget -O %s %s' % (file_path.encode('utf-8'), image_link))


if __name__ == '__main__':
    load_ji(collect, '/Users/lzx/Desktop/%d' % collect)


