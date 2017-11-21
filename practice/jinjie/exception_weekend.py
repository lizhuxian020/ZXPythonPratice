# coding: utf-8
# Author: lee_zix

from utils.log_tools import init_logger
from urllib import urlopen

# 异常习题：
#
# 一
# 编写with操作类Fileinfo()，定义__enter__和__exit__方法。完成功能：
#
# 1.1
# 在__enter__方法里打开Fileinfo(filename)，并且返回filename对应的内容。如果文件不存在等情况，需要捕获异常。
#
# 1.2
# 在__enter__方法里记录文件打开的当前日期和文件名。并且把记录的信息保持为log.txt。内容格式："2014-4-5 xxx.txt"
#
class Fileinfo(object):

    filename = None
    file_handler = None

    def __init__(self, filename):
        self.filename = filename
        pass

    def __enter__(self):
        logger = init_logger('./tmp/exception_weekend.txt', 'exception_weekend')
        if self.filename is not None:
            try:
                self.file_handler = open(self.filename, 'a')
            except Exception, ex:
                print ex
                logger.error('fail to open: %s, \nERROR: %s' % (self.filename, ex))
                return None
            else:
                logger.debug('success to open: %s' % self.filename)
                return self.file_handler
        else:
            print 'there is no filename'
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_handler is not None:
            self.file_handler.close()
        pass

# 二：用异常方法，处理下面需求：
#
# info = ['http://xxx.com', 'http:///xxx.com', 'http://xxxx.cm'....]
# 任意多的网址
#
# 2.1
# 定义一个方法get_page(listindex)
# listindex为下标的索引，类型为整数。 函数调用：任意输入一个整数，返回列表下标对应URL的内容，用try except 分别捕获列表下标越界和url
# 404
# not found
# 的情况。
#


class UrlInfo(object):

    urlinfo = []

    def __init__(self, urlinfo):
        self.urlinfo = urlinfo
        pass

    def get_page(self, listindex):
        try:
            page_url = self.urlinfo[listindex]
            url_obj = urlopen(page_url)
            content = url_obj.read()

        except (IndexError, IOError), ex:
            if (ex.args[0] == 'socket error'):
                logger = init_logger('./tmp/UrlInfo.txt', 'UrlInfo')
                logger.error(self.urlinfo[listindex])
            print ex.args[0]
        else:
            print 'success'
        pass


if __name__ == '__main__':
    # with Fileinfo('./exception_weekend.txt') as f:
    #     if f is not None:
    #         f.write('this is contetn')

    info_ins = UrlInfo(['https://www.baasddasu.com', 'http://www.baidu.com'])
    info_ins.get_page(0)


# 2.2
# 用logging模块把404的url，记录到当前目录下的urlog.txt。urlog.txt的格式为：2013 - 04 - 05
# 15:50:03, 625
# ERROR
# http: // wwwx.com
# 404
# not foud、
#
#
# 三：定义一个方法get_urlcontent(url)。返回url对应内容。
#
# 要求：
#
# 1
# 自己定义一个异常类，捕获URL格式不正确的情况，并且用logging模块记录错误信息。
#
# 2
# 用内置的异常对象捕获url
# 404
# not found的情况。并且print
# 'url is not found'
#
#
#

