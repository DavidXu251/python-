
import numpy as np
import time
import pygame
pygame.init()
width,height=600,500
screen=pygame.display.set_mode(
    (width,height))

while True:
    time.sleep(1/240)
    pygame.event.get()
    pygame.display.flip()
    screen.fill((255,255,255))

    rate=time.time()%2/2
    for x in range(0,width,20):
        for y in range(0,height,20):
            z=0
            
            x1=x
            y1=y
            z1=-(y)/height+1

            x2=x1*rate+x*(1-rate)
            y2=y1*rate+y*(1-rate)
            z2=z1*rate+1*(1-rate)

            x3=x2/z2
            y3=y2/z2
            
            pygame.draw.rect(screen,
                    pygame.Color(0,0,0),
                    pygame.Rect(x3,y3,5,5),
                    0)






    
