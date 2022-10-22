import pygame,random
pp=pygame;dd=pygame.display
ee=pygame.event
size=width,height=600,500
center=cx,cy=int(width*0.5),int(height*0.5)
pp.init()
screen=dd.set_mode(size)
white=255,255,255
continuing=1
x,y=100,100;vx,vy=10,10;mx,my=0,0
vxx=0;vyy=0
def check():
    global ee,pp,continuing,mx,my
    for ev in ee.get():
        if ev.type==12:continuing=False
        if ev.type==pp.MOUSEMOTION:
            mx,my=ev.pos
def drawa(x,y):
    pygame.draw.circle(screen,white,(x,y),10)

while continuing:
    check()
    move()
    screen.fill((0,0,0))
    drawa(x,y)
    drawa(mx,my)
    dd.flip()
pp.quit()
    
