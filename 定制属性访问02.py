# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 定制属性访问02.py
@time: 2018/8/10 10:50
@desc:
'''
# encoding: utf-8


class A:
    att = 'abc'
    def __getattribute__(self, item):
        print("触发了 __getattribut__()")
        return object.__getattribute__(self, item) + ' from getattribute'

    def __getattr__(self, item):
        print("触发了 __getattr__() 方法")
        return item + " form getatter"

    def __get__(self, instance, owner):
        print("触发了 __get__()方法", instance, owner)
        return self

class B:
    a1 = A()

if __name__ == '__main__':
    a2 = A()
    b = B()

    print('————————————————————————————————————————')
    print(a2.att)
    print('————————————————————————————————————————')
    print(a2.ppppppppp)
    print('————————————————————————————————————————')
    b.a1
    print('————————————————————————————————————————')
    print(b.a1.att)