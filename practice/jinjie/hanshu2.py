# coding: utf-8
from urllib import urlopen
import json
import os
#
# 习题：
#
# 1 定义一个方法get_num(num),num参数是列表类型，判断列表里面的元素为数字类型。其他类型则报错，并且返回一个偶数列表：（注：列表里面的元素为偶数）。
def get_num(num):
    if not isinstance(num, list) and not isinstance(num, tuple):
        return 'params %s is not list' % num
    for x in num:
        if not isinstance(x, int):
            return 'list %s is not all int' % repr(num)
    result = [x for x in num if isinstance(x, int) and x % 2 == 0]
    return result
#
# 2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。提示（可以了解python的urllib模块）。
def get_page(url):
    story = urlopen('https://www.python.org')
    data = story.read()
    print('Data:', data.decode('utf-8'))
# story_words = []
# data = story.read()
# print('Status:', story.status, story.reason)
# for k, v in story.getheaders():
#     print('%s: %s' % (k, v))
# print('Data:', data.decode('utf-8'))

# for line in story:
#     line_words = line.split()
#     for words in line_words:
#         story_words.append(words)
#
# 3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。
def func(*params):
    for x in params:
        if not isinstance(x, int):
            print 'element %r is not int' % x
            return
    return 'min: %d, max: %d' % (min(params), max(params))

#
# 4 定义一个方法get_dir(f),f参数为任意一个磁盘路径，该函数返回路径下的所有文件夹组成的列表，如果没有文件夹则返回"Not dir"。

def get_dir(f):
    """test"""
    if not os.path.isdir(f):
        print 'Not dir'
        return
    for x in os.listdir(f):
        print x
    list_dir = [f.rstrip('/')+'/'+i for i in os.listdir(f) if os.path.isdir(f.rstrip('/')+'/'+i)]
    if list_dir == []:
        return 'dir is empty'
    else:
        return list_dir
#
#
# 注明：吸取上次作业遇到的问题，要求写的函数逻辑清楚，并且考虑一些特殊的情况处理，能做断言的尽量用断言。

if __name__ == '__main__':
    # print get_num((1, 2, '3'))
    # get_page('asd')
    # print func(1,2,3,4)
    # print get_dir('usr/')

    print dir(get_dir.__code__)
    print get_dir.__code__.co_varnames
    print get_dir.__code__.co_names
    print get_dir.__code__.co_filename
