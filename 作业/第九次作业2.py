# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 第九次作业2.py
@time: 2018/8/7 12:36
@desc:
'''

class Cla:
    def fun(self, name, age):
        print("我是{}，我今年{} 岁".format(name, age))

    def fun2(n):
        print("类本身的第{}次调用".format(n))
    def fun3(self):
        print("无用函数")

if __name__ == '__main__':

    Cla.fun2(1)
    ll = Cla()
    ll.fun("李雷", 11)

    mm = Cla()
    mm.fun("韩梅梅", 10)

    print("程序最后一行代码~~~~\n____________________________________")