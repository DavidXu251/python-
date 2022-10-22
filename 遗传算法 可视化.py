
import pygame
pygame.init()
width,height=600,500
screen=pygame.display.set_mode((
    width,height))
clock=pygame.time.Clock()

white=(255,255,255)
black=(0,0,0)
blue=(50,153,204)
gray=(230,230,230)

import numpy as np
animals=np.random

while True:
    clock.tick(70)
    pygame.display.flip()
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill(white)
    
    
    















