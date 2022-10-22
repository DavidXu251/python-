

import ctypes
ctypes.windll.user32.SetProcessDPIAware()


import pygame
import numpy as np
from numpy import sin,cos,pi
import time


pygame.init()
width,height=1600,1600
screen=pygame.display.set_mode(
    (width,height))
screen.fill((255,255,255))
ball_count=16

Ox=0
Oy=0
frame=0
while True:
    frame+=1
    time.sleep(1/500)
    pygame.display.flip()
    for eve in pygame.event.get():
        if eve.type==pygame.KEYDOWN:
            print(eve.__dict__)
            screen.fill((255,255,255))
            if eve.unicode=='a':
                Ox-=1
            elif eve.unicode=='d':
                Ox+=1
            elif eve.unicode=='w':
                Oy-=1
            elif eve.unicode=='s':
                Oy+=1
            print(Ox, Oy)

    
    t=frame/150

    for x in range(ball_count):
        for y in range(ball_count):
            screen.set_at(
                ( int( 50+100*x+40*cos((x+Ox)*t) ),
                  int( 50+100*y+40*sin((y+Oy)*t) )
                ),
                (0,0,0)
            )





        

run()
