# coding: utf-8
# Author: lee_zix

def test():

    for i in range(4):
        print 'test1: %d' % i
        yield i
        print 'test: %d' % i

#
if __name__ == '__main__':

    t = test()

    print t
    print t.next()
    # print t.next()

#
