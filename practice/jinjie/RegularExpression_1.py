# coding: utf-8
# Author: lee_zix

import re
# 作业：
#
# 1 已知字符串:
info = '<a href="http://www.baidu.com">baidu</a>'
#
# 用正则模块提取出网址："http://www.baidu.com"和链接文本:"baidu"
match_obj = re.match(r'.*="(.*)".*>(.*)<.*', info)
print dir(match_obj)
print match_obj.string
print match_obj.groups()
#

# 2 字符串："one1two2three3four4" 用正则处理，输出 "1234"
info_1 = 'one1two2three3four4'
split_obj = re.split(r'[a-z]{3,5}', info_1)
print ''.join([x for x in split_obj if len(x) > 0])
#
# 3 已知字符串：text = "JGood is a handsome boy, he is cool, clever, and so on..." 查找所有包含'oo'的单词。
text = "JGood is a handsome boy, he is cool, clever, and so on..."
text_match = re.split(r' ', text)
print [x for x in text_match if 'oo' in x]
#
# 4 为什么在unix里，grep后面的正则有些时候要加引号，有些时候不需要。
