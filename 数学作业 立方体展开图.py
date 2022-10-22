
import pygame

import time
from math import sqrt
import numpy as np

white=255,255,255
black=0,0,0

width,height=1000,375
pygame.init()
screen=pygame.display.set_mode(
    (width,height))
screen.fill(white)

def polygon(string_large):
    for string in string_large.split():
        if string=='':
            continue
        points=[eval(x) for x in string]
        pygame.draw.polygon(screen,black,
            points,2)

    
points=np.array([
    0,0,
    1,0,
    1,1,
    0,1,
    0,2,
    1+sqrt(2),1,
    1+sqrt(2),0,
    -1,0,
    -1,1,
    0,-1,
    ]).reshape((10,2))


points[..., 0]+=1
points[..., 1]+=1
points*=100
points[..., 1]=height-points[..., 1]
points=points.astype('int')

A,B,C,D,E,F,G,H,I,J=points
polygon('''
ABCD
BCFG
ADIH
DCE
ABJ
''')

#第二张
points=np.array([
    0,0,
    1,0,
    1,1,
    2,1,
    1,-sqrt(2),
    1-1/sqrt(2), 1+1/sqrt(2),
    ]).reshape((6,2))


points[..., 0]+=4
points[..., 1]+=1.6
points*=100
points[..., 1]=height-points[..., 1]
points=points.astype('int')

A,B,C,D,E,F=points
polygon('''
ABC
BCD
ABE
ACF
''')


#第三张
points=np.array([
    0,0,
    1,0,
    1,1,
    0,1,
    2,1,
    1,2,
    -sqrt(2),1,
    1,-sqrt(2),
    ]).reshape((8,2))


points[..., 0]+=8
points[..., 1]+=1.6
points*=100
points[..., 1]=height-points[..., 1]
points=points.astype('int')

A,B,C,D,E,F,G,H=points
polygon('''
ABCD
ABH
BCE
CDF
DAG
''')



while True:
    time.sleep(0.01)
    pygame.event.get()
    pygame.display.flip()
