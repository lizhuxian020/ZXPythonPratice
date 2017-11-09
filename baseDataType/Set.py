# coding: utf-8

a = set('abc')
print a

# add
a.add('python')
print a

# update
a.update('python')
print a

# remove
a.remove('python')
print a

# in not in
print 'a' in a
print 'python' in a

# & | -
b = set('wocao')
c = set('caoni')
print b & c
print b | c
print b - c

# 去重
a = [1, 1, 1, 2, 3]
print list(set(a))
