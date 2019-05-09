# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 第十四次作业.py
@time: 2018/8/15 13:36
@desc:
'''
def maker():
    n1 = 1
    n2 = 1
    yield n1
    yield n2
    while True:  #这种方法也行，不过占用cup较多
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        yield n3

if __name__ == '__main__':
    m = maker()
    for i in range(30):
        print("第 {} 个月 ，本月有 {} 只兔子".format(i+1, next(m)))