# coding: utf-8
# Author: lee_zix

import os
import time_tools as time

# 字母表
alphabet = [chr(i) for i in range(97, 123)]


def make_sure_path(path, type):
    """
    make sure the file path existed, if not, create the file path
    :param path:
    :param type: 'f' or 'd'
    :return:
    """
    if os.path.exists(path):
        if type == 'f' and os.path.isfile(path):
            return True
        if type == 'd' and os.path.isdir(path):
            return True
    try:
        if type == 'f':
            if is_path(path, type):
                # 创建空白文件
                write_file(path, '')
            else:
                print 'path: %s is not a file path' % path
        elif type == 'd':
            if is_path(path, type):
                os.makedirs(path)
            else:
                print 'path: %s is not a dir path' % path
    except:
        return False
    else:
        return True


def is_path(path, type):
    """
    judge if path is a file path or direction path, even if it is not exist
    :param path: 路径
    :param type: 'f' or 'd'
    :return: True or False
    """
    if isinstance(path, str) and path.find('/') != -1:
        # 用/来分开, 判断list最后一个带'.'且不以'.'开头, 是否以'./'开头或者以'/'开头
        list_path = path.split('/')
        last_part = list_path[len(list_path)-1]
        fir_part = list_path[0]
        if fir_part.find('/') == 0 or fir_part.find('./'):
            if type == 'd':
                return True
            elif type == 'f' and last_part.find('.') != -1 and last_part.find('.') != 0:
                return True
    return False


def write_file(filename, content):
    """write content to file, if file is not exist, it will create it"""
    try:
        c = open(filename, 'a')  # 'r': read, 'w': write, 'a': append
    except (IOError), e:
        if e.errno == 2:
            file_path = e.filename[:-len(e.filename.split('/')[-1])]
            if make_sure_path(file_path):
                write_file(filename, content)
            else:
                print 'fail to create path: %s' % file_path
                return False
        else:
            print 'could not handle error: %s' % e
    else:
        c.write(content)
        c.close()
        return True
    finally:
        print 'end'


def log(filename, content):
    """log content with standard format"""
    write_file(filename, '\n---------------------------------------------------\n')
    content = '%s   %s' % (time.get_time(), content)
    write_file(filename, content)

if __name__ == '__main__':
    #
    # filepath = './logCache/'
    # filename = 'test.txt'
    #
    # log(filepath+filename, 'haha')

    real_file_path = './log_tool.py'
    fake_file_path = './ad/./asd.txt'

    real_dir_path = './logCache'
    fake_dir_path = './temp1/'

    # print os.path.exists(real_file_path)
    # print os.path.isfile(real_file_path)
    # print os.path.isdir(fake_dir_path)
    # print os.path.isdir(real_dir_path)

    # print os.path.abspath(real_file_path)

    # print isfile_path(fake_file_path)







