# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: 装饰器02.py
@time: 2018/8/11 17:26
@desc:
'''
import logging
level = ''

def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'warn':
                # args 是一个数组, kwargs 是一个字典
                logging.warning('%s is running'% func.__name__)
            elif level == 'info':
                logging.info('{} is running'.format(func.__name__))
            return func(*args)
        return wrapper
    return decorator

'''
上面的user_logging是允许带参数的装饰器。
它实际上是对原有装饰器的一个函数封装，
并返回一个装饰器。
我们可以将它理解为一个含油参数的闭包。
当我们使用 @use_logging(level='warn') 调用时，
python能够发现这一层的封装，并把参数传递到装饰器的环境中。
@use_logging(level='warn') 等价于 @decorator
'''

@use_logging (level = "warn")
# 等价于 @decorator
def foo(name='foo'):
    print('i am {}'.format(name))
    # logging.info('foo id running')





foo()