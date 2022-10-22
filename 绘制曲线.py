
from math import sqrt
from time import sleep

def dis(A,B):
    return sqrt( (A[0]-B[0])**2+(A[1]-B[1])**2 )


A=(250,200)
B=(350,200)
C=(150,400)
D=(450,400)
def f(x,y):
    E=(x,y)
    #val=dis(A,E)
    #val=dis(A,E)+dis(B,E)
    val=dis(A,E)+dis(B,E)+dis(C,E)+dis(D,E)
    return val-700




import pygame
pygame.init()

width,height=600,600
screen=pygame.display.set_mode(
    (width,height))
screen.fill((255,255,255))

for P in [A,B,C,D]:
    pygame.draw.rect(screen,
        pygame.Color(0,0,0),
        pygame.Rect(P,(10,10) ),
        0)
    
y=0
for y in range(height):
    pygame.display.flip()
    pygame.event.get()
    sleep(1/120)
    screen.set_at( (0,y), (0,0,0) )
    for x in range(width):
        val=f(x,y)
        #print(f(x,y))
        #input()
        if abs(val)<=2:
            screen.set_at((x,y),
                    pygame.Color(150,0,150))
    

while True:
    pygame.display.flip()
    pygame.event.get()
    sleep(1/30)

    
