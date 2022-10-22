
import numpy as np
import time

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(True)

import pygame
pygame.init()
width,height=600,256
screen=pygame.display.set_mode(
    (width,height))
screen.fill((255,255,255))

r=20
g=20
b=20
while True:
    time.sleep(1/120)
    pygame.display.flip()
    screen.fill((0,0,0))
    for eve in pygame.event.get():
        if eve.type==pygame.MOUSEBUTTONUP:
            print(r,g,b)
    if pygame.mouse.get_pressed()[0]:
        x,y=pygame.mouse.get_pos()
        y=height-y-1
        #print(y)
        if x<=100:
            r=y
        elif x<=200:
            g=y
        elif x<=300:
            b=y
        color=(r,g,b)
    
    pygame.draw.rect(screen,
        (r,0,0),
        #(255,255-r,255-r),
        (0, height-r,100,height),
        0)
    pygame.draw.rect(screen,
        (0,g,0),
        #(255-g,255,255-g),
        (100, height-g,100,height),
        0)
    pygame.draw.rect(screen,
        (0,0,b),
       #(255-b,255-b, 255),
        (200, height-b,100,height),
        0)
    pygame.draw.rect(screen,
        (r,g,b),
        (300,0,300,300),
        0)
    



    
