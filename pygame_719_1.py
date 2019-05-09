"""
小游戏基础
一只兔子，按F11 全屏
按上下左右移动
撞边折返
"""

import pygame
import sys
from pygame.locals import *  #将pygame所有的常量导入

pygame.init()

size = width,height = 800,550
bg = (0,0,0)  #设置背景色
# bg = (255,255,255)  #设置背景色
screen = pygame.display.set_mode(size, RESIZABLE)  # 设置指定窗口的大小
pygame.display.set_caption("欢迎进入") # 设置标题
tuzi = pygame.image.load("imag/tuzi2.png")  #插入图片
position = tuzi.get_rect() #得到该图片矩形框
clock = pygame.time.Clock() #为设置帧率做准备
speed = [0, 0]

# 设置全屏
fullscreen = False
# 鼠标移动
moving = False
# 兔子头的朝向
left_head  = pygame.transform.flip(tuzi, True, False)
right_head = tuzi
#旋转图片
# down_head =  pygame.transform.rotate(tanke , 90)
# up_head   =  pygame.transform.rotate(tanke , -90)


while True:

    for event in pygame.event.get():#获取事件的集合
        if event.type == pygame.QUIT:#关闭事件
            print("已关闭程序")
            sys.exit()
        if event.type == pygame.KEYDOWN:#键盘按下
            if event.key == K_LEFT:
                speed = [-10, 0]
                tuzi = left_head
            if event.key == K_RIGHT:
                speed = [10, 0]
                tuzi = right_head
            if event.key == K_UP:
                speed = [0, -10]
                # tanke = down_head
            if event.key == K_DOWN:
                speed = [0, 10]
                # tanke = up_head

            # 按下F11，进入全屏模式
            if event.key == K_F11:
                fullscreen = not fullscreen
                #反转，但不能因为上面是FALSE，下面就弄成TRUE，这样的haul第二次按下F11后就没用了
                fenbianlv = pygame.display.list_modes()
                if fullscreen:
                    # size = width, height = fenbianlv[1]
                    # screen = pygame.display.set_mode(fenbianlv[1],FULLSCREEN | HWSURFACE)
                    screen = pygame.display.set_mode(fenbianlv[1],FULLSCREEN)

                else :
                    size = width, height = fenbianlv[15]

                    screen = pygame.display.set_mode(size)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                moving = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                moving = False
        # 拖动窗口，手动调整窗口大小
        if event.type == VIDEORESIZE:
            size = event.size
            width, height = size
            screen = pygame.display.set_mode(size, RESIZABLE)

    # if moving:
        # position = pygame.mouse.get_pos()
    else:
        position = position.move(speed)  # 移动操作

    if position.left < 0 or position.right > width:
        tuzi = pygame.transform.flip(tuzi, True, False)
        #反转函数，第一个参数是图片对象，第二个问你是否要横向反转，第三个问是否纵向反转
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        # tuzi = pygame.transform.flip(tuzi, False, True)

        speed[1] = -speed[1]


    screen.fill(bg) #背景涂刷
    screen.blit(tuzi, position)   #图像显示
    pygame.display.flip()   #刷新
    #pygame.time.delay(10)   #设置延迟
    clock.tick(60) #镇率为30
