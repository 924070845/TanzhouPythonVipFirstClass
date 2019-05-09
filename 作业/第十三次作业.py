# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 第十三次作业.py
@time: 2018/8/14 13:47
@desc:
'''
try:
    print(1/0)
except Exception as e:
    print(e)
finally:
    raise NameError("finally里面的内容")