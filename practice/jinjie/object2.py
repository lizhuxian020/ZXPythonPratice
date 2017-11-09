# coding: utf-8
# Author: lee_zix

# 习题：
#
# 定义一个列表的操作类：Listinfo

class ListInfo(object):
    def __init__(self, param_list):
        self.param_list = param_list

    #
    # 包括的方法:
    #
    # 1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
    def add_key(self, keyName):
        if not isinstance(self.param_list, list):
            print 'params_list: %s is not list' % repr(self.param_list)
            return False
        self.param_list.append(keyName)
        return True

    # 2 列表元素取值：get_key(num) [num:整数类型]
    def get_key(self, num):
        if not isinstance(self.param_list, list):
            print 'params_list: %s is not list' % repr(self.param_list)
            return None
        if not isinstance(num, int):
            print 'param: %s is not int' % repr(num)
            return None
        return self.param_list[num]

    # 3 列表合并：update_list(list)	  [list:列表类型]
    def update_list(self, param_list):
        if not isinstance(self.param_list, list):
            print 'params_list: %s is not list' % repr(self.param_list)
            return None
        if not isinstance(param_list, list):
            print 'param: %s is not list' % repr(param_list)
            return None
        self.param_list.extend(param_list)

    # 4 删除并且返回最后一个元素：del_key()
    def del_key(self):
        if not isinstance(self.param_list, list):
            print 'params_list: %s is not list' % repr(self.param_list)
            return None
        return self.param_list.pop()


#
# list_info = Listinfo([44,222,111,333,454,'sss','333'])
#
# 定义一个集合的操作类：Setinfo
#

class SetInfo(object):
    def __init__(self, param_set):
        self.param_set = param_set

# 包括的方法:
#
# 1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
    def add_setinfo(self, keyname):
        if not isinstance(self.param_set, set):
            print 'param_set: %s is not set' % repr(self.param_set)
            return False
        self.param_set.add(keyname)
        return True

# 2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
    def get_intersetion(self, unioninfo):
        if not isinstance(self.param_set, set):
            print 'param_set: %s is not set' % repr(self.param_set)
            return None
        if not isinstance(unioninfo, set):
            print 'param: %s is not set' % repr(unioninfo)
            return None
        return self.param_set.intersection(unioninfo);


# 3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
    def get_union(self, unioninfo):
        if not isinstance(self.param_set, set):
            print 'param_set: %s is not set' % repr(self.param_set)
            return None
        if not isinstance(unioninfo, set):
            print 'param: %s is not set' % repr(unioninfo)
            return None
        return self.param_set.union(unioninfo)

# 4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]
    def del_difference(self, unioninfo):
        if not isinstance(self.param_set, set):
            print 'param_set: %s is not set' % repr(self.param_set)
            return None
        if not isinstance(unioninfo, set):
            print 'param: %s is not set' % repr(unioninfo)
            return None
        return self.param_set.difference(unioninfo)
#
# set_info =  Setinfo(你要操作的集合)

if __name__ == '__main__':
    list_info = ListInfo([44, 222, 111, 333, 454, 'sss', '333'])

    print list_info.param_list

    list_info.add_key('asd')

    print list_info.param_list

    print list_info.get_key(3)

    print list_info.del_key()

    print list_info.param_list

    list_info.update_list(['asd', 'qwe'])

    print list_info.param_list

    print list_info

    set_info = SetInfo(set('wocao'))

    print set_info.param_set

    print set_info.add_setinfo('ad')

    print set_info.param_set

    print set_info.get_intersetion(set('woca'))

    print set_info.get_union(set('wori'))

    print set_info.param_set

    print set_info.del_difference(set('ri'))
