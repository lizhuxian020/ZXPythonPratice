# coding: utf-8
# Author: lee_zix

"""
1. lambda的使用
2. filter方法
"""


def zx_filter(x):
    z, y = x
    return z > 0


def person_desc(name = None, **otherDesc):
    otherDesc_list = ['%s: %s' % (k, v) for k, v in otherDesc.items()]
    otherDesc_list.insert(0, name)
    print ', '.join(otherDesc_list)

if __name__ == '__main__':
    b = lambda x: x + 1
    print b(1)
    print b(2)

    c = lambda x: x + 1 if x > 0 else 'error'
    print c(-4)
    print c(4)

    d = lambda x: [(x, i) for i in range(10)]
    print d(10)

    t = [(0, 2), (1, 2), (1, 2), (1, 2), (1, 2)]
    t_filt = filter(zx_filter, t)
    print t_filt

    person_desc('lee_zix', year = 3, tolk = 176)
