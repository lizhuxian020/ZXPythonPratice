# coding=utf-8

fileName = 'test.txt'

c = open(fileName, 'w')  # 'r': read, 'w': write, 'a': append
c.write('this is content')
c.close()

c = open(fileName, 'r')
print c.read()
c.close()

# multiLine
fileName = 'multiLine.txt'
c = open(fileName, 'w')
c.write('asdas\nwocoa\nahah\n')
c.close()

c = open(fileName, 'r')
print c.read()
c.close()

c = open(fileName, 'w')
print >> c, 'eoeklkdfsdkf',
print >> c, 'eoeklkdfsdkf',
c.close()


# 一行一行读取
import linecache

print linecache.getline(fileName, 1)
print linecache.getline(fileName, 2)
print linecache.getline(fileName, 3)
# 获得list
print linecache.getlines(fileName)
