# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 第七次作业.py
@time: 2018/8/2 11:08
@desc:
'''

def fun(argument):
    if type(argument) != str and type(argument) != list and type(argument) != tuple:
        print("请输入序列类型参数")
    else:
        return len(argument)

if __name__ == '__main__':
    a = fun(123)
    b = fun({'2':123})
    c = fun({1, 2, 3})
    d = fun("1234")
    print(d)
    e = fun((1, 2, 3 ,4 ,5))
    print(e)
    f = fun([1, 2, 3, 4, 5, 6])
    print(f)
    g = fun("1, 2, 3, ,4, 5, 6, 7")
    print(g)
