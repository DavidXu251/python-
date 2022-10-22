



from p5 import *
import numpy as np
from numpy import sin,cos,pi
import time


def setup():
    size(800,800)

ball_count=8

start_t=time.time()
frame=0

def draw():
    global t,frame
    
    t=(time.time()-start_t)/2
    frame+=1
    if frame==1:
        background(255)
    if frame%60==0:
        print('fps=',frame/t)

    f=frame/120
    no_fill()
    stroke(150,0,150)
    for x in range(ball_count):
        for y in range(ball_count):
            
            point(
                int( 50+100*x+40*cos(x*f) ),
                int( 50+100*y+40*sin(y*f) )
            )
            
            pass






        

run()
