# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 第十次作业.py
@time: 2018/8/8 11:08
@desc:
'''
class Cls:
    def __repr__(self):
        print('我是注释')
        return "注释在哪里"

    def __str__(self):
        return '触发str方法'

ins = Cls()
#执行 str(ins) 返回了“触发 str 方法”
#打印返回值
print(str(ins))
#执行了repr(ins),将返回值赋值给 i
i = repr(ins)
print(i)
