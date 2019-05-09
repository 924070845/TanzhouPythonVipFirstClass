# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 推导表达式.py
@time: 2018/8/15 10:19
@desc:
'''
'''
向列表中添加100个元素的几种做法
'''
# No.1
li1 = []
for i in range(1, 101):
    li1.append(i)
# print(li1)

# No.2
li2 = [i for i in range(1, 101)]
# print(li2)

# 挑出偶数,以及不要4
li3 = []
for i in range(1, 101):
    if i % 2 == 0:
        if i !=4:
            li3.append(i)
# print(li3)

li3 = [i for i in range(1, 101) if i % 2 == 0 if i !=4 ]
# print(li3)

# 字典的表达式
# 在值的部分以键值对的形式出现

# li0 = [('k1', 'v1'),('k2', 'v2')]
# dic0 = {k: v for k, v in li0}
# print(dic0)

# dic2 = {str(i) : 000 for i in range(1, 10)}
# print(dic2)

# 三目运算
# li1 = [i if i % 2 == 0 else "奇数" for i in range(1, 20) ]
# print(li1)

dic = {str(i) : str("奇数" if i % 2 != 0 else "偶数") for i in range(1, 11)}
print(dic)
# print(dic)
