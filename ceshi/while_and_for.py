# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: while_and_for.py
@time: 2018/8/1 8:15
@desc:
'''
print("作业一")
for i in range(8):
    for j in range(i+1):
        print('##', end="")
    print()


print("作业二")
for i in range(31):
    if i !=7 and i % 7 != 0 and i % 10 != 7 or i == 0:
        if i % 2 == 0:
            print("{} 是偶数".format(i))
        else:
            print("{} 是奇数".format(i))


