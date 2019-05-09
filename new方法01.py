# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: new方法01.py
@time: 2018/8/9 11:38
@desc:
'''

class Cls:

    instance_xq = 0

    def __new__(cls, *args, **kwargs):

        if cls.instance_xq == 0:
            cls.instance_xq = super().__new__(cls)
            return cls.instance_xq
        else:
            return cls.instance_xq

    def fun(self, n):
        print("这里的n是:{}".format(n))

c1 = Cls()
c2 = Cls()
c3 = Cls()
c4 = Cls()

print(id(c1))
print(id(c2))
print(id(c3))
print(id(c4))
print(type(c1))
print(type(c2))
print(type(c3))
print(type(c4))







#
#
# c1.name = 'f'
# c2.name = 'd'
# c3.name = 'fd'
# print(c1, c2, c3)