# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 7-01.py
@time: 2018/8/17 21:06
@desc:
'''
def fun(arg1):

    try:
        if type(arg1) != str:
            raise Exception("参数不是字符串")
        else:
            print('参数是字符串')
            dic = {}
            for i in set(arg1):
                dic[i] = arg1.count(i)
            print(dic)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    s = 'qqqqq1wwww22eee333rr4444t55555'
    fun(s)

