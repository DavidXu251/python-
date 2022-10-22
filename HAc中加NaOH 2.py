


from math import sqrt
import time
import numpy as np

import pygame
width,height=600,500
pygame.init()
screen=pygame.display.set_mode(
    (width,height))
screen.fill((255,255,255))
clock=pygame.time.Clock()


Na=0
OH=0
H=0
HAc=1
Ac=0
data=np.zeros((width,5))

while True:
    for x,(Na,OH,H,HAc,Ac) in enumerate(data):
        screen.set_at((x,int(H*height)),(0,0,0))
    pygame.display.flip()
    pygame.event.get()
    clock.tick(60)
    
    




