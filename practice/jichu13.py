# coding: utf-8
# ##习题1：
#
#
# 列表a = [11,22,24,29,30,32]
a = [11, 22, 24, 29, 30, 32]
# 1 把28插入到列表的末端]
a.append(28)
# 2 在元素29后面插入元素57
a.insert(4, 57)
# 3 把元素11修改成6
a[0] = 6
# 3 删除元素32
a.pop(a.index(32))
# 4 对列表从小到大排序
a.sort(reverse=True)
print a
#
#
# ##习题2：
#
#
# 列表b = [1,2,3,4,5]
b = [1, 2, 3, 4, 5]
# 1 用2种方法输出下面的结果：
# [1,2,3,4,5,6,7,8]
b.extend([6, 7, 8])
# 2 用列表的2种方法返回结果：[5,4]
print list([b.pop(), b.pop()])
# 3 判断2是否在列表里
if 2 in b:
    print 'is in b'
print b
#
#
# ##习题3：
#
#
b = [23, 45, 22, 44, 25, 66, 78]
# 用列表解析完成下面习题：
# 1 生成所有奇数组成的列表
print [x for x in b if x % 2 == 1]
# 2 输出结果: ['the content 23','the content 45']
print ['this content %d' % x for x in b if (x == 23 or x == 45)]
# 3 输出结果: [25, 47, 24, 46, 27, 68, 80]
# print [ x for x in b if x =x + 2]
c = []
for x in b:
    c.append(x + 2)
print c
c = [x + 2 for x in b]
print c

#
#
# ##习题4：
# 用range方法和列表推导的方法生成列表：
# [11,22,33]
def giss(x):
    if x >= 10:
        ge = x % 10
        shi = int(x / 10)
        return ge == shi
    return False


print [x for x in range(100) if giss(x)]
#
#
#
#
# ##习题5：
#
#
# 已知元组:a = (1,4,5,6,7)
a = (1, 4, 5, 6, 7)
# 1 判断元素4是否在元组里
if 4 in a:
    print '4 in a'
#
# 2 把元素5修改成8
b = list(a)
b[2] = 8
print tuple(b)
#
#
# ##习题6：
#
#
# 已知集合:setinfo = set('acbdfem')和集合finfo = set('sabcdef')完成下面操作：
setinfo = set('acbdfem')
finfo = set('sabcdef')
# 1 添加字符串对象'abc'到集合setinfo
setinfo.add('abc')
# 2 删除集合setinfo里面的成员m
setinfo.remove('m')
# 3 求2个集合的交集和并集
print setinfo & finfo
print setinfo | finfo
print setinfo
#
#
# ##习题7：
#
#
# 用字典的方式完成下面一个小型的学生管理系统。
#
#
# 1 学生有下面几个属性：姓名，年龄，考试分数包括：语文，数学，英语得分。
# 比如定义2个同学：
chinese = 'chinese'
math = 'math'
eng = 'eng'
name = 'name'
age = 'age'
score = 'score'
# 姓名：李明，年龄25，考试分数：语文80，数学75，英语85
liming = {age: 25, name: 'liming', score: {chinese: 80, math: 75, eng: 85}}
# 姓名：张强，年龄23，考试分数：语文75，数学82，英语78
zhangqiang = {age: 23, name: 'zhangqiang', score: {chinese: 75, math: 82, eng: 78}}
# 2 给学生添加一门python课程成绩，李明60分，张强：80分
python = 'python'
liming[score].update({python: 60})
zhangqiang[score].update({python: 80})
# 3 把张强的数学成绩由82分改成89分
zhangqiang[score][math] = 89
#
#
# 4 删除李明的年龄数据
del liming[age]
# 5 对张强同学的课程分数按照从低到高排序输出。
scoreList = zhangqiang[score].values()
scoreList.sort()
print scoreList
#
#
# 6 外部删除学生所在的城市属性，不存在返回字符串 beijing
print zhangqiang.get('city', 'beijing')
print zhangqiang.pop('city', 'beijing')

print '{1} is a {0}'.format('i', 'wcoa')


print liming
print zhangqiang

