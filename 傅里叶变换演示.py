size = width, height = 600, 500
printtime = 0
white = 255, 255, 255
black = 0, 0, 0
screenX, screenY = 0, 0
actors = []
text_size = 50

def nothing(*args): pass


def SquareAve(a, b):
    return (a ** 2 + b ** 2) ** 0.5


for _ in [0]:
    import pygame
    pygame.init()
    screen = pygame.display.set_mode(size)
    findevent = pygame.event.get
    import time
    game_start_time=time.time()
    import random
    pygame.font.init()
    worder=pygame.font.SysFont('',text_size)
def newlife(flips=1):
    global actors, screen
    pygame.display.flip()
    screen.fill((0, 0, 0))
    global mouse, printtime
    for eve in findevent():
        if eve.type == 1:  # 鼠标进入这个窗口
            pass
        elif eve.type == 4:  # 鼠标移动
            mouse = eve
        elif eve.type == 12:  # 退出键
            print('显示了', printtime, '次')
            all_time= time.time() - game_start_time
            average_fps=printtime/all_time
            print('显示了',all_time,'秒')
            print('平均帧数:',average_fps,'张/秒')
            pygame.quit()
            import sys
            sys.exit()
        else:
            pass
    printtime += 1
##    for x in actors:
##        screen+x+x+x+x+x+x+x+x+x+x+x+x
    for _ in range(10):
        for x in actors:
            screen+x
newlife()

class block:
    def __init__(self, Sx, Sy, name='no name',
                 Vx=0., Vy=0., Ax=0., Ay=0., Vmax=3.,
                 Lx=15., Ly=15.,Aair=0.,
                 drag=False,bound=False,vanish=False):
        self.Sx = Sx
        self.Sy = Sy
        self.name = name
        self.color = 255, 255, 255
        self.Vx, self.Vy = Vx, Vy
        self.Ax, self.Ay = Ax, Ay
        self.Vmax = Vmax
        self.Lx, self.Ly = Lx, Ly
        self.drag, self.dragged = drag, False
        self.Aair=Aair
        self.bound=bound
        self.vanish=vanish
    ##        if name=='sky':
    ##            self.color=white=255,255,255
    ##        if name=='wood':
    ##            self.color=brown=150,75,0
    def goto(self, x):
        self.Sx, self.Sy = x
    def __radd__(self, scr):
        global screenX, screenY, mouse, nothing
        self.Vx, self.Vy = (self.Ax + self.Vx), (self.Ay + self.Vy)
        if self.Aair!=0.0:
            self.V=(self.Vx**2+self.Vy**2)**0.5
            Aair=self.Aair*self.V
            if Aair>=self.V:
                self.Vx=self.Vy=0
            else:
                AairX=Aair/self.V*self.Vx
                AairY=Aair/self.V*self.Vy
                self.Vx-=AairX
                self.Vy-=AairY
        self.Vx, self.Vy = min(self.Vx, self.Vmax), min(self.Vy, self.Vmax)
        self.Sx, self.Sy = (self.Sx + self.Vx), (self.Sy + self.Vy)
        if self.bound:
            global width,height
            if self.Sx+self.Lx>=width:
                self.Vx=-abs(self.Vx)
            if self.Sx<=0:
                self.Vx=abs(self.Vx)
            if self.Sy+self.Ly>=height:
                self.Vy=-abs(self.Vy)
            if self.Sy<=0:
                self.Vy=abs(self.Vy)
        if self.drag:
            self.clicked = (
                    -self.Lx < mouse.pos[0] - self.Sx < self.Lx
                    and -self.Ly < mouse.pos[1] - self.Sy < self.Ly
                    and mouse.buttons[0] == 1)
            if self.clicked:
                self.dragged = True
                self.color = (255, 0, 0)
            if mouse.buttons[0] == 0:
                self.dragged = False
                self.color = (255, 255, 255)
            if self.dragged:
                self.goto(mouse.pos)
        pygame.draw.rect(scr, self.color,
                         (self.Sx - screenX, self.Sy - screenY
                          , self.Lx, self.Ly), 0)
        if self.vanish:
            if not 0 < self.Sy < height:
                self.__add__ = self.__radd__ = nothing
            elif not 0 < self.Sx < width:
                self.__add__ = self.__radd__ = nothing
        return scr
    __add__=__radd__

class dots:
    def __init__(self, array, Sx=0, Sy=height,
                 color=white):
        self.array = array
        self.Sx, self.Sy = Sx, Sy
        self.color = color

    def __radd__(self, screen):
        x = self.Sx
        for y in self.array:
            x += 1
            y = self.Sy - y
            screen.set_at((x, y), self.color)
        return scr



class button:
    def __init__(self):
        pass
    def __radd(self,scr):
        return scr


#############
class drawboard:
    def __init__(self):
        pass
    def __radd__(self,scr):
        return scr
class rope:
    def __init__(self, obj1, obj2,
                  lenth=10 ,Ast=1,
                 width=1, color=white):
        self.obj1=obj1
        self.obj2=obj2
        self.width=width
        self.Ast=Ast
        self.lenth=lenth
        self.color=color
    def xlen(self):
        return self.obj2.Sx-self.obj1.Sx
    def ylen(self):
        return self.obj2.Sy - self.obj1.Sy
    def __radd__(self,scr):
        xlen,ylen=self.xlen(),self.ylen()
        lenth = (xlen**2+ylen**2)**0.5
        if lenth==0:lenth=0.001

        A=lenth-self.lenth
        A=A*0.0001*self.Ast
        A=max(A,0)
        Ax=A*xlen/lenth
        Ay=A*ylen/lenth
        self.obj1.Vx +=Ax
        self.obj1.Vy +=Ay
        self.obj2.Vx -=Ax
        self.obj2.Vy -=Ay
        pygame.draw.line(scr,
                self.color,
                (self.obj1.Sx,self.obj1.Sy),
                (self.obj2.Sx,self.obj2.Sy),
                 self.width)
        return scr
    __add__=__radd__
class text:
    def __init__(self,word='aaaa',
                 size=20,color=white):
        self.pic=worder.get
##画出sin的动画#############
##import numpy as np
##a=np.linspace(start=30,stop=200,num=7)
##a=dots(a)
##num=0
##while True:
##    num+=1
##    a=np.linspace(start=0,stop=3.14*3,num=num)
##    a=np.sin(a)*75
##    a=dots(a,Sy=height/2)
##    screen+a
##    newlife()
##############################
a=block(20,20)
b=a
actors.append(a)
all_blocks=[b]
for x in range(20):
    d=block(5*x,40,drag=True,
            Aair=0.001,Ay=0.001,Ax=0.001,
            bound=True,Vmax=1000)
    c=rope(b,d,lenth=0)
    actors.extend((d,))
    all_blocks.append(d)
    b=d


while True:
    newlife()
    a.Sx,a.Sy=mouse.pos
    a.Vx=a.Vy=0
    for blo in all_blocks:
        blo.Vx+=random.randint(-1,1)/10
        blo.Vy+=random.randint(-1,1)/10
