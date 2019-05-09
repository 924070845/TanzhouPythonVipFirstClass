# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 九九乘法表.py
@time: 2018/8/5 8:44
@desc:
'''
def fun():
    a = 1
    for i in range(9):
        b = 1
        for j in range(i+1):
            s = a * b
            print('{} * {} = {}'.format(a,b,s), end='\t')
            b +=1
        print()

        a += 1

if __name__ == '__main__':
    fun()