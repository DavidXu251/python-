
import time
from numpy import log
import numpy as np

def linspace(start,end,size):
    return np.linspace(start,end,size+1)[:-1]

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(True)

import pygame
pygame.init()

width,height=64*9*3, 64*3
screen=pygame.display.set_mode((width,height))
screen.fill((255,255,255))




size=height

while True:
    color_std=np.random.randint(256//3+1,256*2//3,size=3)
    print( np.sum((color_std-128)**2) )
    color_strong=(color_std-128)*3+128
    r,g,b=color_strong
    print(color_std)
    print(color_strong)
    print(list(
        np.average([[r,128,128],[128,g,128],[128,128,b]],axis=0)))
    print()


    
    screen.fill((255,255,255))
    pygame.draw.rect(screen,
        color_std,
        (0,0,size,size),
        0)
    pygame.draw.rect(screen,
        color_std,
        (width-size,0,size,size),
        0)
    for splits, x in enumerate(range(size,width-size,size)):
        splits=2**splits
        for y in linspace(0,height,splits):
            for i,y_part in enumerate(linspace(y,y+size/splits,3)):
                color=[128]*3
                color[i]=[r,g,b][i]
                pygame.draw.rect(screen,
                    color,
                    [int(a) for a in [x, y_part, size, size/splits/3]],
                    0)
            pygame.display.flip()
            pygame.event.get()
            time.sleep(1/120)

    time.sleep(3)


        
                    
                         
        
        
        
    



