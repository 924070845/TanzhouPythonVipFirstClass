# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: list_01.py
@time: 2018/7/31 9:53
@desc:
'''

li1 = [1, 2, 3, 4]
li2 = [3, 4, 5, 6]
list1 = set(li1)
list2 = set(li2)
print(list1)
print(list2)
print("方法一：")
print((list1&list2))
print("方法二：")
for i in li1:
    for j in li2:
        if i == j:
            print(i, end=" ")
