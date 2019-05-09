# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 第九次作业.py
@time: 2018/8/7 12:21
@desc:
'''

class Cla:
    name = 'xuanqing'
    age = 20

cla = Cla()
print("————————————————\n实例对属性的增删查改")
cla.sex = '男'
print("增加的属性：" + cla.sex)
del cla.sex
cla.name = '玄青'
n = cla.name
print("查出修改过的属性：" + n)
print("————————————————\n类对属性的增删查改")
Cla.group = 29
print("增加的属性：%s" % Cla.group)
del Cla.group
Cla.name  = "张三"
n = Cla.name
print("查出修改过的属性：" + n)

