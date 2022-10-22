
import numpy as np
import time

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(True)

import pygame
pygame.init()
width,height=600,600
screen=pygame.display.set_mode(
    (width,height))
screen.fill((255,255,255))

while True:    
    screen.fill((255,255,255))
    pygame.draw.rect(screen,
        (0,0,0),
        (0,0,size,size),
        0)



    
