# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 5-01.py
@time: 2018/8/17 16:34
@desc:
'''
def fun():
    ppp = []
    print("请输入一个序列，判断这个序列是升序、降序还是无序")
    print("输入 # 表示输入结束")

    while True :
        s = input()
        ppp.append(s)
        if s == '#':
            ppp.pop()
            break

    if ppp == sorted(ppp):
        print("UP")
    elif ppp == sorted(ppp, reverse=True):

        print('DOWN')
    else:
        print("None")

if __name__ == '__main__':
    fun()