# coding: utf-8
# Author: lee_zix

import urllib

def normal_exception():

    sth_url = 'http://asdasd'


    try:
        url_obj = urllib.urlopen(sth_url)
    except:
        print '抛出异常'
    else:
        url_content = url_obj.read()
        print url_content
        url_obj.close()
    finally:
        print 'qie'


# 1 定义一个函数func(filename) filename:文件的路径，函数功能：打开文件，并且返回文件内容，最后关闭，用异常来处理可能发生的错误。

#
# 2 定义一个函数func(urllist)   urllist:为URL的列表，例如：['http://xx.com','http://www.xx.com','http://www.xxx.com'...]
#
# 函数功能：要求依次打开url，打印url对应的内容，如果有的url打不开，则把url记录到日志文件里，并且跳过继续访问下个url。
#
# 3 定义一个函数func(domainlist)   domainlist:为域名列表，例如：['xx.com','www.xx.com','www.xxx.com'...]
# 函数功能：要求依次ping 域名，如果ping 域名返回结果为：request time out，则把域名记录到日志文件里，并且跳过继续ping下个域名。（提示用os模块的相关方法）


if __name__ == '__main__':

    normal_exception()
