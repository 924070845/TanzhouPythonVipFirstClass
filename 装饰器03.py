# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 装饰器03.py
@time: 2018/8/11 21:45
@desc:
'''
'''
函数和函数调用是有区别的，函数是指整个函数体，
但是在python中，函数也可以作为其他函数的参数被调用，
函数被调用，意味着此时该函数的值是其返回值
'''
def decorator_a(func):
    print ('Get in decorator_a')
    def inner_a(*args, **kwargs):
        print ('Get in inner_a')
        return func(*args, **kwargs)    #在 inner 函数里调用了 func 函数，将func 的调用结果，作为值返回
    return inner_a
    #返回的这个 inner 是函数对象，它在上面被定义过了


def decorator_b(func):
    print ('Get in decorator_b')
    def inner_b(*args, **kwargs):
        print ('Get in inner_b')
        return func(*args, **kwargs)
    return inner_b

@decorator_b
@decorator_a
def f(x):
    print ('Get in f')
    return x * 2

'''
@decorator_a
def f(x):
    print ('Get in f')
    return x * 2


# 相当于
def f(x):
    print ('Get in f')
    return x * 2

f = decorator_a(f)
'''


s = f(1)
# print(s)
