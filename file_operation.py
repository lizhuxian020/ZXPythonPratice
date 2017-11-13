# coding=utf-8
import os

fileName = './haha/heihei/test.txt'


def make_sure_path(path):
    if os.path.exists(path):
        return True
    try:
        os.makedirs(path)
    except:
        return False
    else:
        return True

def write_file(filename):
    try:
        c = open(filename, 'w')  # 'r': read, 'w': write, 'a': append
    except (IOError), e:
        if e.errno == 2:
            file_path = e.filename[:-len(e.filename.split('/')[-1])]
            if make_sure_path(file_path):
                write_file(filename)
            else:
                print '创建文件夹: %s 失败' % file_path
    else:
        c.write('this is content')
        c.close()
    finally:
        print 'end'

write_file(fileName)


# c = open(fileName, 'r')
# print c.read()
# c.close()
#
# # multiLine
# fileName = 'multiLine.txt'
# c = open(fileName, 'w')
# c.write('asdas\nwocoa\nahah\n')
# c.close()
#
# c = open(fileName, 'r')
# print c.read()
# c.close()
#
# c = open(fileName, 'w')
# print >> c, 'eoeklkdfsdkf',
# print >> c, 'eoeklkdfsdkf',
# c.close()
#
#
# # 一行一行读取
# import linecache
#
# print linecache.getline(fileName, 1)
# print linecache.getline(fileName, 2)
# print linecache.getline(fileName, 3)
# # 获得list
# print linecache.getlines(fileName)
