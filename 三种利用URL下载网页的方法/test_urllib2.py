# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: test_urllib2.py
@time: 2018/8/22 21:39
@desc:
'''
import urllib2

url = 'http://www.baidu.com'
print ('第一种方法')
response1 = urllib2.urlopen(url)
print(response1.getcode())
print(len(response1.read()))







def fun(self):
    pass


if __name__ == '__main__':
    pass