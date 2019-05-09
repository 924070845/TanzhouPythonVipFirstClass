# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 4-01.py
@time: 2018/8/17 15:55
@desc:
'''
import re
def fun (string):
    ss = re.findall(".+?", string)
    sss = set(ss)
    iter1 = iter(sss)
    print('\"字符串由', end='')
    for i in range(len(sss)):
        s1 = iter1.__next__()
        print(s1, end=', ')
    print('\"组成')

if __name__ == '__main__':
    s = 'akbfkhkcabs'
    fun(s)
