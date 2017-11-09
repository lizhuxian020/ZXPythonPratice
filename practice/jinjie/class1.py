# coding: utf-8
# Author: lee_zix

# 面向对象习题：
#
# 一：定义一个学生类。有下面的类属性：
#
# 1 姓名
# 2 年龄
# 3 成绩（语文，数学，英语)[每课成绩的类型为整数]

class student(object):

    def __init__(self, name = '', age = '', score = []):
        self.name = name
        self.age = age
        self.score = score

        print self.get_age()
        print self.get_course()
        print self.get_name()

    def get_name(self):
        """get student's name"""
        return self.name

    def get_age(self):
        """get student's age"""
        return self.age

    def get_course(self):
        """get the highest score of student"""
        if not isinstance(self.score, list) and not isinstance(self.score, tuple):
            print '%s is not list or tuple' % repr(self.score)
            return None
        return max(self.score)



#
# 类方法：
#
# 1 获取学生的姓名：get_name() 返回类型:str

# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
#
#
# 写好类以后，可以定义2个同学测试下:
#
# zm = student('zhangming',20,[69,88,100])
# 返回结果：
# zhangming
# 20
# 100
#
# lq = student('liqiang',23,[82,60,99])
#
# 返回结果：
# liqiang
# 23
# 99
#
#
#
# 二：定义一个字典类：dictclass。完成下面的功能：
#
#
# dict = dictclass({你需要操作的字典对象})

class dictClass(object):

    def __init__(self, dic):
        self.param_dic = dic

    def del_dict(self, key):
        if not isinstance(self.param_dic, dict):
            print 'param_dic %s is not dict' % repr(self.param_dic)
            return False
        if self.param_dic.has_key(key):
            del self.param_dic[key]
            return True
        return False

    def get_dict(self, key):
        if not isinstance(self.param_dic, dict):
            print 'param_dic %s is not dict' % repr(self.param_dic)
            return None
        if self.param_dic.has_key(key):
            return self.param_dic[key]
        return 'not found'

    def get_key(self):
        if not isinstance(self.param_dic, dict):
            print 'param_dic %s is not dict' % repr(self.param_dic)
            return None
        return self.param_dic.keys()

    def update_dict(self, param_dic):
        if not isinstance(self.param_dic, dict):
            print 'param_dic %s is not dict' % repr(self.param_dic)
            return None
        self.param_dic.update(param_dic)
        return self.param_dic.values()
#
# 1 删除某个key
#
# del_dict(key)
#
#
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
#
# get_dict(key)
#
# 3 返回键组成的列表：返回类型;(list)
#
# get_key()
#
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
#
# update_dict({要合并的字典})
#
#

if __name__ == '__main__':

    zix = student('lee_zix', 18, [100, 150, 120])

    dic = dictClass({'a': 123, 'b': 234})

    print dic.param_dic

    # dic.del_dict('a')
    print dic.get_dict('a')

    print dic.get_key()

    print dic.update_dict({'c': 456})


    print dic.param_dic