#   创建三个同心圆，颜色为红绿蓝，鼠标点击可拖动

import pygame
import sys
from pygame.locals import *

pygame.init()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

size = width, height = 650, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("欢迎进入")

position = size[0]//2, size[1]//2
moving = False

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                moving = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                moving = False

    if moving:
        position = pygame.mouse.get_pos()

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED , position, 25, 1)
    pygame.draw.circle(screen, GREEN , position, 75, 1)
    pygame.draw.circle(screen, BLACK , position, 125, 1)

    pygame.display.flip()

    clock.tick(120)
