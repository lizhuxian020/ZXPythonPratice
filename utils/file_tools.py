# coding: utf-8
# Author: lee_zix

import os
import time_tools as time


def make_sure_path(path):
    """make sure the file path existed, if not, create the file path"""
    if os.path.exists(path):
        return True
    try:
        os.makedirs(path)
    except:
        return False
    else:
        return True


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

    filepath = './logCache/'
    filename = 'test.txt'

    log(filepath+filename, 'haha')
