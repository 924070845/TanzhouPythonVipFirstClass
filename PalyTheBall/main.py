# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: main.py
@time: 2018/7/21 8:26
@desc:
'''

import pygame
import sys
from pygame.locals import *
from random import *

# 初始化函数
class Ball(pygame.sprite.Sprite):   # 球类继承自Sprite类
    def __init__(self, image, position, speed):
        pygame.sprite.Sprite.__init__(self) # 初始化动画精灵
        self.image = pygame.image.local(image).convert_alpha()
        #图片支持透明转换,所有的图片都加上 convert_alpha()会有利于你的游戏速度
        self.rect = self.image.get_rect()   #获得图片所在的矩形框
        self.rect.left, self.rect.top = position    #定义位置，将小球放到指定的位置
        self.speed = speed  #speed本以为速率、加速


def main():
    pygame.init()
    ball_image = ""


