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
# print dir(match_obj)
# print match_obj.string
print match_obj.groups()
#

# 2 字符串："one1two2three3four4" 用正则处理，输出 "1234"
info_1 = 'one1two2three3four4'
asd = re.match(r'[a-z]+([0-9])', info_1)
print asd.groups()
# split_obj = re.split(r'[a-z]{3,5}', info_1)
# print ''.join([x for x in split_obj if len(x) > 0])
#
# 3 已知字符串：text = "JGood is a handsome boy, he is cool, clever, and so on..." 查找所有包含'oo'的单词。
text = "JGood is a handsome boy, he is cool, clever, and so on..."
text_match = re.split(r' ', text)
print [x for x in text_match if 'oo' in x]
#
# 4 为什么在unix里，grep后面的正则有些时候要加引号，有些时候不需要。
# 已知字符串：
#
info_2 = 'test,&nbsp;url("http://www.baidu.com")&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com">ininnnin<img src="http://www.dd.com">'
#
# 要求完成下面2个小功能：
# 1.1 关闭[img]标签
# 1.2 将url()中的["]转为[']
#
# 最后结果字符串：
#
# "test,&nbsp;url('http://www.baidu.com')&,dddddd "="" <svg></svg><path></path><img src="http://www.baidu.com"></img>ininnnin<img src="http://www.dd.com"></img>"
print '------------------------------------------------'
m = re.match(r'(\w+) (\w+)!(\w+)(?P<wocao>.{2})', 'hello world!asd')
print 'm', m
print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup

print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(3)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\2 \1\g<wocao>'):", m.expand(r'\2 \1\g<wocao>')

p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)

print p.match('helo world!asd', 3).groups()
print "p.pattern:", p.pattern
print "p.flags:", p.flags
print "p.groups:", p.groups
print "p.groupindex:", p.groupindex