# coding: utf-8

# Extend: 在a的基础上拼接
a = [1, 2, 3]
b = [4, 5, 6]
print a + b     # 这个会生成新的List, 增大内存
a.extend(b)
print a

# insert: 在a的基础上直接插入b
a = [1, 2, 3]
b = [4, 5, 6]
a.insert(2, b)
print a

# append: 在a的末尾直接insert
a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
print a

# 列表推导式
# .得到1-10列表
print [x for x in range(1, 11)]
# .得到1-10的奇数列表
print [x for x in range(1, 11) if x % 2 == 1]
# .得到1-100平方值
print [x-1 for x in range(1, 101)]
# .以下杂七杂八的推导式
print ['the %d' % x for x in range(1, 10)]
# .元组
print [(x, y) for x in range(3) for y in range(2)]
# .字典
print dict([(x, y) for x in range(3) for y in range(3)])