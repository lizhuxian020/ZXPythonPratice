# coding: utf-8
# 一.已经字符串
# s = "i,am,lilei", 请用两种办法取出之间的“am”字符。

s = "i,am,lilei"
print s.split(',')[1]
print s[2:4]

#
# 二.在python中，如何修改字符串？

#
# 三.bool("2012" == 2012)
# 的结果是什么。False
print bool("2012" == 2012)

#
# 四.已知一个文件
# test.txt，内容如下：
#
# ____________
# 2012
# 来了。
# 2012
# 不是世界末日。
# 2012
# 欢乐多。
# _____________
#
# 1.
# 请输出其内容。
fileName = 'test.txt'
txt = open(fileName, 'r')
content = txt.read()
txt.close()
print content
# 2.
# 请计算该文本的原始长度。
print len(content.decode('utf-8'))
# 3.
# 请去除该文本的换行。
contentWithoutReturn = content.replace('\n', '')
print contentWithoutReturn
# 4.
# 请替换其中的字符
# "2012"
# 为
# "2013"。
print contentWithoutReturn.replace('2012', '2013')
# 5.
# 请取出最中间的长度为5的子串。

print '------------------------di5'
decodeContent = contentWithoutReturn.decode('utf-8')
print decodeContent[len(decodeContent)/2:len(decodeContent)/2+5].encode('utf-8')
print '------------------------end'
# 6.
# 请取出最后2个字符。
contentWithoutReturn += '12'
print contentWithoutReturn[-2:]
# 7.
# 请从字符串的最初开始，截断该字符串，使其长度为11.
print contentWithoutReturn[:11]
# 8.
# 请将
# {4}
# 中的字符串保存为test1.py文本.
newFileName = 'test1.py'
o = open(newFileName, 'w')
o.write(contentWithoutReturn.replace('2012', '2013'))
o.close()
#
# 五.请用代码的形式描述python的引用机制。
#
# 六.已知如下代码
#
# ________
#
a = "中文编程"
b = a
c = a
a = "python编程"
# b = u'%s' % a
d = "中文编程"
e = a
c = b
b2 = a.replace("中", "中")
# ________
#
# 1.
# 请给出str对象
# "中文编程"
# 的引用计数
import sys
print sys.getrefcount(a)
# 2.
# 请给出str对象
# "python编程"
# 的引用计数
#
# 七.已知如下变量
# ________
a = "字符串拼接1"
b = "字符串拼接2"
# ________
#
# 1.
# 请用四种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣。
print a + b
print '%s%s' % (a, b)
print '{a}{b}'.format(a=a, b=b)
print ''.join([a, b])
# 2.
# 请将a与b拼接成字符串c，并用逗号分隔。
ab = a + ',' + b
print ab
# 3.
# 请计算出新拼接出来的字符串长度，并取出其中的第七个字符。
print len(ab.decode('utf-8'))
print ab.decode('utf-8')[7]
#
#
# 八.请阅读string模块，并且，根据string模块的内置方法输出如下几题的答案。
#
# 1.
# 包含0 - 9
# 的数字。
print '123'.isdigit()
# 2.
# 所有小写字母。
print 'abA'.islower()
# 3.
# 所有标点符号。

# 4.
# 所有大写字母和小写字母。
# 5.
# 请使用你认为最好的办法将
# {1} - {4}
# 点中的字符串拼接成一个字符串。
#
# 九.已知字符串
# ________
#
# a = "i,am,a,boy,in,china"
# ________
#
# 1.
# 假设boy和china是随时可能变换的，例boy可能改成girl或者gay，而china可能会改成别的国家，你会如何将上面的字符串，变为可配置的。
a = "i,am,a,{sexy},in,{country}".format(sexy='boy', country='china')
# 2.
# 请使用2种办法取出其间的字符
# "boy"
# 和
# "china"。
# 3.
# 请找出第一个
# "i"
# 出现的位置。
print a.find('i')
# 4.
# 请找出
# "china"
# 中的
# "i"
# 字符在字符串a中的位置。
print a.find('i', a.find('china'))
# 5.
# 请计算该字符串一共有几个逗号。
print a
print a.count('i')
#
#
# 十.请将模块string的帮助文档保存为一个文件。