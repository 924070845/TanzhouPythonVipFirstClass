# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 文件操作.py
@time: 2018/8/17 22:08
@desc:
'''
import io

def fun():

    """
    流的操作
    :return:
    """
    sio = io.StringIO()
    sio.writelines(input("请输入："))
    file = open('log.txt', mode='r', encoding='utf-8')

    # f = file.read()
    # print(f)
    print(sio.getvalue())
    file.flush()
    file.close()


def fun2():
    """
    为了读和写同时进行
    :return:
    """
    with open('log.txt', mode='a+', encoding='utf-8') as file:
        file.write(input("请输入："))
    with open('log.txt', mode='r+', encoding='utf-8') as file:
        print(file.read())


if __name__ == '__main__':
    # fun()
    fun2()