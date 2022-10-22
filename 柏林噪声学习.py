

import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import math
import numpy as np
import matplotlib.pyplot as plt
import time

def perlin(x,y,seed=0):
    # permutation table
    np.random.seed(seed)
    p = np.arange(256,dtype=int)
    np.random.shuffle(p)
    p = np.stack([p,p]).flatten()
    # coordinates of the top-left
    xi = x.astype(int)
    yi = y.astype(int)
    # internal coordinates
    xf = x - xi
    yf = y - yi
    # fade factors
    u = fade(xf)
    v = fade(yf)
    # noise components
    n00 = gradient(p[p[xi]+yi],xf,yf)
    n01 = gradient(p[p[xi]+yi+1],xf,yf-1)
    n11 = gradient(p[p[xi+1]+yi+1],xf-1,yf-1)
    n10 = gradient(p[p[xi+1]+yi],xf-1,yf)
    # combine noises
    x1 = lerp(n00,n10,u)
    x2 = lerp(n01,n11,u) # FIX1: I was using n10 instead of n01
    return lerp(x1,x2,v) # FIX2: I also had to reverse x1 and x2 here

def lerp(a,b,x):
    "linear interpolation"
    return a + x * (b-a)

def fade(t):
    "6t^5 - 15t^4 + 10t^3"
    return 6 * t**5 - 15 * t**4 + 10 * t**3

def gradient(h,x,y):
    "grad converts h to the right gradient vector and return the dot product with (x,y)"
    vectors = np.array([[0,1],[0,-1],[1,0],[-1,0]])
    g = vectors[h%4]
    return g[:,:,0] * x + g[:,:,1] * y


width=height=1000

def reset_noise():
    global noise1, noise2
    lin = np.linspace(0,2,width, endpoint=False)
    x,y = np.meshgrid(lin,lin) # FIX3: I thought I had to invert x and y here but it was a mistake
    noise1=0.01*perlin(x,y,
                      seed=np.random.randint(0, 2**31-1))
    noise2=0.01*perlin(x,y,
                      seed=np.random.randint(0, 2**31-1))
reset_noise()
plt.imshow(noise1, origin='upper', cmap='gray')




import pygame
screen=pygame.display.set_mode(
    (width,height))
screen.fill((255,255,255))
Sx, Sy=100,0
Vx, Vy=0,0
frame_count=0

while True:
    frame_count+=1
    time.sleep(1/300)
    Vx+=noise1[int(Sx), int(Sy)]
    Vy+=noise2[int(Sx), int(Sy)]
    Vx=math.tanh(Vx/10)*10.05
    Vy=math.tanh(Vy/10)*10.05
    
    Sx+=Vx
    Sy+=Vy
    
    if (not 0<Sx<width) or (not 0<Sy<height):
        Sx=np.random.randint(0,width)
        Sy=0
        Vx=0
        Vy=0
    
    screen.set_at((int(Sx), int(Sy)),
                  (0,0,0))
    pygame.display.flip()
    pygame.event.get()
