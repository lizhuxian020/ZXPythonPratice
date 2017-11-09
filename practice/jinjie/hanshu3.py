# coding: utf-8
# Author: lee_zix
import types

# 今天习题：
#
# 1 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"
def get_fundoc(func):
    if isinstance(func, types.FunctionType):
        desc = func.__doc__
        if isinstance(desc, types.NoneType) or len(desc) == 0:
            return 'not found'
        return func.__doc__
    else:
        return 'func %s is not function' % repr(func)

#
# 2 定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。
def get_cjsum():
    num_sum = 0
    for index, item in enumerate(range(1, 101)):
        num_sum += item * item
    return num_sum

#
# 3 定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行一些相关的操作，不会影响到原来列表的元素值，比如：
#
# a = [1,2,3]
#
# def list_info(list):
#    '''要对list进行相关操作，不能直接只写一句return[1,2,5]，这样就没意义了'''
#
# print list_info(a):返回结果：[1,2,5]
#
# print a 输出结果：[1,2,3]
#
# 写出函数体内的操作代码。
def list_info(params):
    if not isinstance(params, list):
        print 'params: %s is not list' % repr(params)
        return
    return [x+1 for x in params]
#
#
# 4 定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，如果可以调用则返回该函数名(
# 类型为str)，否则返回 “fun is not function"。
def get_funcname(func):
    """
    get function isValidate
    :param func: Function
    :return: BOOL
    """
    if not isinstance(func, types.FunctionType):
        print 'params: %s is not function' % repr(func)
        return False
    print dir(func)
    print dir(func.__code__)
    
    print func.func_name


if __name__ == '__main__':
    # print get_fundoc('asd')
    # print get_cjsum()

    # a = [1, 2, 3]
    # print list_info(a)
    # print a
    get_funcname(get_cjsum)

