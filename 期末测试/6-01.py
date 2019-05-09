# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 6-01.py
@time: 2018/8/17 17:45
@desc:
'''
def fun(arg1, arg2):
    try:
        if type(arg1) != list:
            raise TypeError(" 参数类型出错啦，重新传参")
        elif type(arg2) != dict:
            raise TypeError(" 参数类型出错啦，重新传参")

        if len(arg1) == len(arg2):
            print("请输入不等长的列表和字典 ")
        else:
            dic_len = len(arg2)
            a = 0
            for i in arg1:
                arg1[a] = dic_len
                a += 1
            values = list(arg2.values())
            new_li = values
            values = arg1
            arg1 = new_li
            key = arg2.keys()
            arg2 = dict(zip(key, values))
            print(arg1)
            print(arg2)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    a = [1, 3, 5, 7, 9]
    b = {'a':1, 'b':2, 'c':3}
    fun(a, b)
