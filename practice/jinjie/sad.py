# coding: utf-8
# Author: lee_zix

def test():

    for i in range(4):
        print 'test1: %d' % i
        yield i
        print 'test: %d' % i


def fblq_num(num):
    """斐波拉切数列"""
    ls = [0, 1]
    result = ls[-1] + ls[-2]
    while num >= result:
        ls.append(result)
        result = ls[-1] + ls[-2]
        # yield result


    return ls
    pass


def fibonacci(num):
    x, y = 0, 1
    f = [x]
    while y <= num:
        f.append(y)
        x, y = y, x+y
    else:
        return f
    pass


def is_zhi(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num > 1:
        for i in xrange(2, num):
            if num % i == 0:
                return False
        return True
    pass
#
if __name__ == '__main__':
    #
    # t = test()
    #
    # print t
    # print t.next()
    # print t.next()

    # print fblq_num(13)
    # print fibonacci(5)

    print [x for x in xrange(0, 100) if is_zhi(x)]


#
