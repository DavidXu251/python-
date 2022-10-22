
import numpy as np

import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import time

import pygame
pygame.init()
#hello
width,height=800,800
screen=pygame.display.set_mode(
    (width,height))
screen.fill((250,250,250))
pygame.display.flip()

import pygame.freetype
pygame.freetype.init()
#72 default
pygame.freetype.set_default_resolution(200)
font=pygame.freetype.Font(
    '微软雅黑.ttf', size=20, )

lines=['']
lines_img=[]

while True:
    font.render_to(screen, (0,0), 'hello')
    time.sleep(1/120)
    pygame.display.flip()
    pygame.event.get()
    





