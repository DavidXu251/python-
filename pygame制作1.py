size = width, height = 600, 500

import time
frame_count = 0

screenX, screenY = 0, 0
actors = []
text_size = 36

bkg_color=(255,255,255)
def nothing(*args): pass


def SquareAve(a, b):
    return (a ** 2 + b ** 2) ** 0.5


for _ in [0]:
    import pygame
    pygame.init()
    screen = pygame.display.set_mode(size)
    import time
    game_start_time=time.time()
    import random
    pygame.font.init()
    font=pygame.font.SysFont('',text_size)
def newlife(flips=1):
    global eve
    global actors, screen
    pygame.display.flip()
    screen.fill(bkg_color)
    global mouse, frame_count
    mouse.pos=mouse.Sx,mouse.Sy=pygame.mouse.get_pos()
    mouse.pressed=pygame.mouse.get_pressed()
    mouse.down=[0,0,0,0,0,0]
    mouse.up=[0,0,0,0,0,0,]
    for eve in pygame.event.get():
        if eve.type == 1:  # 鼠标进入这个窗口
            pass
        elif eve.type==2: #键盘按下
            eve.key=='a'
        elif eve.type==3: #键盘弹回
            chr(eve.key)=='a'
        elif eve.type == 4:  # 鼠标移动
            mouse.rel=eve.rel
        elif eve.type==5: #鼠标按下
            mouse.down[eve.button-1]=True
        elif eve.type==6: #鼠标松开
            mouse.up[eve.button-1]=True
        elif eve.type == 12:  # 退出键
            print('显示了', frame_count, '次')
            all_time= time.time() - game_start_time
            average_fps=frame_count/all_time
            print('显示了',all_time,'秒')
            print('平均帧数:',average_fps,'张/秒')
            pygame.quit()
            import sys
            sys.exit()
        else:
            print('type=',eve.type,eve)
    frame_count += 1
##    for x in actors:
##        screen+x+x+x+x+x+x+x+x+x+x+x+x
    for _ in range(flips):
        for x in actors:
            screen+x

class block:
    def __init__(self, Sx=0., Sy=0., name='no name',
                 Vx=0., Vy=0., Ax=0., Ay=0., Vmax=3.,
                 Lx=15., Ly=15.,Aair=0., color=(0,0,0),
                 drag=False,bound=False,vanish=False,
                 fixed=False,follow=False):
        global actors
        self.Sx = Sx
        self.Sy = Sy
        self.name = name
        self.real_color=self.color = color
        if fixed:
            self.real_color=0,0,255
        self.Vx, self.Vy = Vx, Vy
        self.Ax, self.Ay = Ax, Ay
        self.Vmax = Vmax
        self.Lx, self.Ly = Lx, Ly
        self.drag, self.dragged = drag, False
        self.Aair=Aair
        self.bound=bound
        self.vanish=vanish
        if fixed==False:
            self.fixed=False
        elif fixed==True:
            self.fixed=(None,None,0,0,0,0)
        elif len(fixed)<=6:
            fixed=list(fixed)
            fixed.extend([0]*(6-len(fixed)))
            self.fixed=fixed
        self.follow=follow
    ##        if name=='sky':
    ##            self.color=white=255,255,255
    ##        if name=='wood':
    ##            self.color=brown=150,75,0
    def goto(self, x):
        self.Sx, self.Sy = x
    def __move__(self):
        self.real_color=self.color
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

        if self.fixed!=False:
            self.Sx,self.Sy,self.Vx,self.Vy,self.Ax,self.Ay=[
                (x if x!=None else origin) for x,origin in
                zip(self.fixed,(self.Sx,self.Sy,self.Vx,self.Vy,self.Ax,self.Ay))]
            self.real_color=0,0,255
        
        self.Sx, self.Sy = (self.Sx + self.Vx), (self.Sy + self.Vy)
        
        if self.fixed!=False:
            self.Sx,self.Sy,self.Vx,self.Vy,self.Ax,self.Ay=[
                (x if x!=None else origin) for x,origin in
                zip(self.fixed,(self.Sx,self.Sy,self.Vx,self.Vy,self.Ax,self.Ay))]
            self.real_color=0,0,255
        
        if self.drag:
            if mouse.down[0] == 1:
                self.clicked=(0< mouse.pos[0] - self.Sx < self.Lx
                              and 0< mouse.pos[1] - self.Sy < self.Ly)
            else:
                self.clicked=False
            if self.clicked:
                self.dragged = True
                self.drag_delta_x=mouse.pos[0] - self.Sx
                self.drag_delta_y=mouse.pos[1] - self.Sy
            if mouse.up[0] == 1:
                self.dragged = False
                self.drag_delta_x=0
                self.drag_delta_y=0
            if self.dragged:
##                self.Sx=mouse.pos[0]-self.drag_delta_x
##                self.Sy=mouse.pos[1]-self.drag_delta_y
                self.Sx=mouse.pos[0]-self.drag_delta_x
                self.Sy=mouse.pos[1]-self.drag_delta_y
                self.real_color=(255,0,0)
        if self.follow:
            self.Sx,self.Sy=mouse.pos
            self.real_color=0,255,255

        
        if self.vanish:
            if not 0 < self.Sy < height:
                self.__add__ = self.__radd__ = nothing
            elif not 0 < self.Sx < width:
                self.__add__ = self.__radd__ = nothing
    def __show__(self,scr):
        pygame.draw.rect(scr, self.real_color,
                         (int(self.Sx - screenX), int(self.Sy - screenY),
                          int(self.Lx), int(self.Ly)), 0)
    def __radd__(self,scr):
        self.__move__()
        self.__show__(scr)
        return scr
    __add__=__radd__

class dots:
    def __init__(self, array, Sx=0, Sy=height,
                 color=(0,0,0)):
        global height,actors,numpy

        import numpy
        #pygame点不支持小数
        #Sx Sy 自动转化成整数
        #array需要手动转化
        self.array = array
        self.Sx, self.Sy = int(Sx), int(Sy)
        self.color = color
        
    def __radd__(self, screen):
        x = self.Sx
        for y in self.array:
            y = self.Sy - y
            screen.set_at((x, y), self.color)
            x+=1
        return screen
    __move__=__show__=__add__=__radd__


class button:
    def __init__(self):
        pass
    def __radd__(self,scr):
        return scr


#############
class drawboard:
    def __init__(self):
        pass
    def __radd__(self,scr):
        return scr

class text(block):
    def __init__(self,text='a',buffer=True,**args):
        block.__init__(self,**args)
        self.text=text
        self.buffer=buffer
        self.picture=font.render(self.text,self.buffer,self.color)
        self.Lx,self.Ly=self.picture.get_size()
    def __show__(self,scr):
        scr.blit(self.picture,(int(self.Sx),int(self.Sy)) )
    


        
class rope:
    def __init__(self, obj1, obj2,
                  length=10 ,Ast=1,
                 width=1, color=(0,0,0)):
        self.obj1=obj1
        self.obj2=obj2
        self.width=width
        self.Ast=Ast
        self.length=length
        self.color=color
    def xlen(self):
        return self.obj2.Sx-self.obj1.Sx
    def ylen(self):
        return self.obj2.Sy - self.obj1.Sy
    def __radd__(self,scr):
        xlen,ylen=self.xlen(),self.ylen()
        length = (xlen**2+ylen**2)**0.5
        if length==0:length=0.001

        A=length-self.length
        A=A*0.0001*self.Ast
        A=max(A,0)
        Ax=A*xlen/length
        Ay=A*ylen/length
        self.obj1.Vx +=Ax
        self.obj1.Vy +=Ay
        self.obj2.Vx -=Ax
        self.obj2.Vy -=Ay
        pygame.draw.line(scr,
                self.color,
                (int(self.obj1.Sx),int(self.obj1.Sy)),
                (int(self.obj2.Sx),int(self.obj2.Sy)),
                 int(self.width))
        return scr
    __add__=__radd__

class ice(block):
    def __init__(self,color=(100,100,255),
                 *args,**kwargs):
        block.__init__(self,color=color,
                *args,**kwargs)
    def __radd__(self,scr):
        self.Vx=self.Vy=self.Ax=self.Ay=0
        self.__show__(scr)
#final setup:
mouse=ice();   actors.append(mouse)
newlife()
#end

blocks=[block(Sx=x,Sy=height/2)
        for x in range(15,width-15,15)]

blocks.insert(0,ice(Sx=0,           Sy=height/2))

blocks.append(ice(Sx=width-15,Sy=height/2))

ropes=[rope(left,right,length=0,Ast=100)
       for left,right in zip(blocks[:-1],blocks[1:])]
actors.extend(blocks+ropes)

head=blocks[0]
from time import sleep
from math import cos
while True:
    newlife()
    if mouse.pressed[0]:
        mid=len(blocks)//2
        blocks[mid].Sy-=4
    sleep(0.005)



        
