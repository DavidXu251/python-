

def dis(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2) **0.5


import time

import pygame
pygame.init()

print(pygame.display.Info())

width,height=2736//2, 1824//2
screen=pygame.display.set_mode((width,height))
screen.fill((255,255,255))
pygame.display.flip()

blue=(10,150,200)
gray=(240,240,240)

x1,y1=0+200,height//2
x2,y2=width-200, height//2
q1=1
q2=-2
Px,Py=-1,-1
print(f'''两个点电荷大小：{q1},{q2}
距离：{abs(x2-x1)}''')

pygame.draw.rect(screen,
        blue,
        pygame.Rect(x1-10,y1-10,20,20),
        0
)
pygame.draw.rect(screen,
        blue,
        pygame.Rect(x2-10,y2-10,20,20),
        0
)
    
while True:
    time.sleep(0.008)
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            exit()
        elif eve.type==pygame.MOUSEBUTTONDOWN:
            Px,Py=eve.pos

    if not -width<Px<2*width:
        Px=Py=-1
    if not -height<Py<2*height:
        Px=Py=-1
    if Px!=-1 and Py!=-1:
        s1=dis(Px,Py,x1,y1)
        s2=dis(Px,Py,x2,y2)
        if s1==0 or s2==0:
            Px=Py=-1
    if Px!=-1 and Py!=-1:
        k=q0=1
        F1= (k*q0*q1)/(s1**2)     #正数为引力
        F2= (k*q0*q2)/(s2**2)     #负数为斥力
        
        Fx=F1/s1*(Px-x1)+F2/s2*(Px-x2)
        Fy=F1/s1*(Py-y1)+F2/s2*(Py-y2)
        F=dis(0,0,Fx,Fy)
        scale_Fx=Fx/F*4
        scale_Fy=Fy/F*4

        Px0, Py0 = Px, Py
        Px+=scale_Fx
        Py+=scale_Fy

        pygame.draw.line(screen,
            blue,
            (int(Px0), int(Py0)),
              (int(Px),   int(Py)),
            2
        )
    
    for i in range(0,50,2):
        screen.set_at((10,i),(0,0,0))
    pygame.display.flip()
    




