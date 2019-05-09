# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 第八次作业.py
@time: 2018/8/3 12:10
@desc:
'''

def fun(li,dic):
    if type(li) != list :
        print('参数类型错误！')
    elif type(dic) != dict:
        print('参数类型错误！')
    elif len(li) != len(dic):
        print("你好")
    else:
        value = list(dic.values())
        print("传入的原参数：");
        print("字典：{}".format(dic))
        print('列表：{}'.format(li))
        print("dic字典的value值：{}".format(value) )
        print("list参数的列表内容：{}".format(li) )

        print("____________________________________")
        print('列表的值和字典的value值互换后：')

        #交换属性
        new_li = value
        value = li
        li = new_li
        print("dic字典的value值：{}".format(value))
        print("list参数的列表内容：{}".format(li))

        print("____________________________________")
        print('最新的列表和字典：')
        key = dic.keys()
        dic = dict(zip(key,value))
        print("新的字典：{}".format(dic))
        print('新的列表：{}'.format(li))
        return li, dic


if __name__ == '__main__':
    fun([1, 2 ,3 ,4],{'a':5, 'b':6, 'c':7, 'd':8})
    print("__________↓错误参数测试↓___________")

    fun([1, 2, 3], {'a': 5, 'b': 6, 'c': 7, 'd': 8})
    fun({'a':4, 'b':5}, [1, 2, 3])
    fun("123", [1, 2, 3])
    fun({'a':4, 'b':5}, "123")
    fun("asd", 123)