
import numpy as np
from numpy import cross

#import ctypes
#ctypes.windll.shcore.SetProcessDpiAwareness(True)

import pygame
pygame.init()
width,height=600,500
screen=pygame.display.set_mode((
    width,height))
screen.fill((255,255,255))

mat=np.array([
    [1,0,0],
    [0,1,0],
    [0.05,0.02,1],
])
points=[]

for x0 in range(0,width//10):
    for y0 in range(0,height//10):
        x,y,z=np.matmul(mat,[x0,y0,1])
        x,y=x/z, y/z
        points.append((x,y))
        screen.set_at((int(x*10),int(y*10)), (0,0,0))
        pygame.display.flip()
        pygame.event.get()































O=(0,0,1)
A=(3,0,1)
B=(0,3,1)
E=(1,1,1)
O,A,B,E=np.array((O,A,B,E))

C=cross(cross(O,A),cross(B,E))
D=cross(cross(O,B),cross(A,E))
print(C,D)





