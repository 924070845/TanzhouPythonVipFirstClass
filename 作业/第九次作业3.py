# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 第九次作业3.py
@time: 2018/8/7 17:31
@desc:
'''

class Cla:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("初始化成功")

    def __del__(self):
        print("调用销毁~")

if __name__ == '__main__':

    mm = Cla("韩梅梅", 10)
    ll = Cla("李  雷", 11)
    bzr = Cla("班主任", 40)
    del bzr
    xz = Cla("校长", 50)

    print("程序最后一行代码~~~~\n————————————————")

