import pygame
import sys
from random import randrange
from pygame.locals import *

class Weights(pygame.sprite.Sprite):
    def __init__(self, speed):
        pygame.sprite.Sprite.__init__(self) 
        self.speed = speed 
        # 绘制Sprite对象时要用到的图像和矩形：
        self.image = weightImage 
        self.rect = self.image.get_rect() 
        self.reset()
        
    def reset(self):
        # 将铅锤移到屏幕顶端的一个随机位置：
        self.rect.top = -self.rect.height 
        self.rect.centerx = randrange(screenSize[0])

    def update(self):
        # 移动铅锤：
        self.rect.top += self.speed 
        # 如果铅锤移出屏幕，则重置：
        if self.rect.top > screenSize[1]:
            self.reset()
        print(f"Weight position: {self.rect.top}, {self.rect.centerx}")  # 调试输出

# 初始化pygame
pygame.init()  
screenSize =  800, 600  # 设置窗口大小
pygame.display.set_mode(screenSize)  # 显示窗口
pygame.mouse.set_visible(1) # 显示光标

# 加载铅锤图像
weightImage = pygame.image.load('D:\\CrashCourse\\Manuscript\\Assignment08\\weight.png') 
weightImage = weightImage.convert() # 以便与显示匹配

speed = 1  # 铅锤移动速度

sprites = pygame.sprite.RenderUpdates() 
sprites.add(Weights(speed))  # 加入铅锤

# 获取并填充屏幕表面
screen = pygame.display.get_surface() 
bg = (255, 255, 255) # 白色
screen.fill(bg) 
pygame.display.flip() # 刷新显示

# 用于清除Sprite对象：
def clearCallback(surf, rect): 
    surf.fill(bg, rect)

clock = pygame.time.Clock()  # 控制循环频率

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
        if event.type == pygame.KEYDOWN:  # 如果按下键盘，则退出
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    sprites.clear(screen, clearCallback)  # 清除屏幕上的Sprite对象
    sprites.update()  # 更新Sprite对象
    updates = sprites.draw(screen)  # 绘制Sprite对象
    pygame.display.update(updates)  # 刷新显示
    clock.tick(60)  # 控制循环频率