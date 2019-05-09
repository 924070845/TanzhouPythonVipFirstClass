# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 正则01.py
@time: 2018/8/15 20:33
@desc:
'''
import re

st1 = "this is a dog \t do you know"
ss2 = re.findall('is*', st1)
print(ss2)