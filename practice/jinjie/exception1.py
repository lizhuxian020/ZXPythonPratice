# coding: utf-8
# Author: lee_zix

import urllib
import utils.file_tools as file_tools
import os
import sys

def normal_exception():

    sth_url = 'http://asdasd'

    try:
        url_obj = urllib.urlopen(sth_url)
    except:
        exc = sys.exc_info()
        print exc  # 捕获全部异常
        print exc[1]  # 异常的message
        print '抛出异常'
    else:
        url_content = url_obj.read()
        print url_content
        url_obj.close()
    finally:
        print 'qie'


# 1 定义一个函数func(filename) filename:文件的路径，函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误。

def open_file(fileName):

    try:
        open_obj = open(fileName, 'r')
    except:
        print '打开不开啊'
    else:
        content = open_obj.read()
        print content
    finally:
        print 'whatever'


#
# 2 定义一个函数func(urllist)   urllist:为URL的列表，例如：['http://xx.com','http://www.xx.com','http://www.xxx.com'...]
#
# 函数功能：要求依次打开url，打印url对应的内容，如果有的url打不开，则把url记录到日志文件里，并且跳过继续访问下个url。
def func_urllist(urllist):

    if not isinstance(urllist, list) and not isinstance(urllist, tuple):
        print 'params: %s is not list or tuple' % repr(urllist)
        return None
    for url in urllist:
        try:
            url_obj = urllib.urlopen(url)
        except (IOError ,ZeroDivisionError), x:
            print 'url_error'
            file_tools.log('./openUrlCache/error/openUrlError.txt', '\nURL: %s, \nError: %s' % (url, x))
        else:
            print 'url_success'
            content = url_obj.read()
            file_tools.log('./openUrlCache/content/openUrlContent.txt', 'URL: %s, Content: %s' % (url, content))
            url_obj.close()
        finally:
            print 'finish'

#
# 3 定义一个函数func(domainlist)   domainlist:为域名列表，例如：['xx.com','www.xx.com','www.xxx.com'...]
# 函数功能：要求依次ping 域名，如果ping 域名返回结果为：request time out，则把域名记录到日志文件里，并且跳过继续ping下个域名。（提示用os模块的相关方法）
def ping_domain(domainlist):
    if not isinstance(domainlist, list) and not isinstance(domainlist, tuple):
        print 'param: %s is not list or tuple' % repr(domainlist)
        return None
    for domain in domainlist:
        popen_obj = os.popen('ping %s' % domain)
        print popen_obj.read()



if __name__ == '__main__':

    # normal_exception()

    # file_path = '../test.txt'
    # open_file(file_path)

    # func_urllist(['http://www.baidu.com', 'http://www.aksjdlasd.com'])

    ping_domain(['baidu.com', 'weibo.com'])



