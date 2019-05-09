# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: str_01.py
@time: 2018/7/31 9:13
@desc:
'''
s1 = "ni hao xuan qing"
s2 = s1.split()
print("s1是 :"+s1)
print("s2是 :{}".format(s2))
print("s1的类型是{}".format(type(s1)) )
print("s2的类型是{}".format(type(s2)) )

for i in s2:
    if i != " ":
        x = s2.index(i)
        print(s2[x],  end = "\t")
        print(type(s2[x]))


