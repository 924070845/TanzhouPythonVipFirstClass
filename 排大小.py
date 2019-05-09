# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 排大小.py
@time: 2018/8/5 9:09
@desc:
'''
def fun():
    print("下面请依次输入三个数：")
    a = int(input("请输入第一个数"))
    b = int(input("请输入第二个数"))
    c = int(input("请输入第三个数"))

    s = []
    s.extend([a, b ,c])
    s.sort()
    print("从小到大的顺序为：")
    for i in s:
        print(i,end='\t')

if __name__ == '__main__':
    fun()