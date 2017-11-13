# coding: utf-8
# Author: lee_zix

import time


def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
