# coding: utf-8
# Author: lee_zix

from utils.file_tools import make_sure_path

root_dir = './WXRes/'

def create_dir():
    for x in range(1, 7):
        for y in range(1, 13):
            path = root_dir + 'grade_%d/' % x + 'unit_%d' % y
            if make_sure_path(path, 'd'):
                print 'success'
            else:
                print 'fail: %s' % path
    for x in range(1, 3):
        for y in range(2, 5):
            path = root_dir + 'grade_%d/' % x + 'Project_%d' % y
            if make_sure_path(path, 'd'):
                print 'success'
            else:
                print 'fail: %s' % path
    pass

if __name__ == '__main__':
    create_dir()