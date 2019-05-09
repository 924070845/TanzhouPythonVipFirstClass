# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 异常01.py
@time: 2018/8/14 11:16
@desc:
'''

try:
    print(aaa)
    # print("aaa")
except Exception as e:# 重命名的 e 是异常信息
    print(e)
    print("异常捕获到的语句1")
else:
    print("异常捕获到的语句2")
finally:
    print("异常捕获到的语句3")
print("执行我不？")