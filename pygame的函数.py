from pygame制作1 import *
#模拟沙子
def sand_box():
    def make_move(a):
        b=[0]*(len(a)+2)
        for place,delta in enumerate(a):
            b[place]+=delta/3
            b[place+1]+=delta/3
            b[place+2]+=delta/3
        return b
    a=[10000]+[0]*100+[5000]
    while True:
        a=make_move(a)
        if len(a)>600:
            a=a[1:-1]
        if 0<mouse.pos[0]<len(a) and mouse.buttons[0]:
            a[mouse.pos[0]]+=mouse.pos[1]/10
        for _ in range(10):
            screen+dots(a,Sy=20)
        newlife()
#画出sin的动画#############
def draw_sin():
    import numpy as np
    a=np.linspace(start=30,stop=200,num=7)
    a=dots(a)
    num=0
    while True:
       num+=1
       a=np.linspace(start=0,stop=3.14*3,num=num)
       a=np.sin(a)*75
       a=dots(a,Sy=height/2)
       screen+a
       newlife()
############################
def fly_blocks():
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
def neckless():
    global width,height
    a=block(Sx=0,Sy=height/2,
            fixed=(None,None,0,0,0,0),drag=True)
    b=block(Sx=width-15,Sy=height/2,
            fixed=(width-15,height/2,0,0,0,0),drag=True)
    block_list=[]
    #width=600
    for x,word in zip(range(10),'morming'):
        block_list.append(
            text(Sx=x*60,Sy=height/2-100,Aair=0.003,
                  Ay=0.01,drag=True,bound=True,text=word))
    actors.extend(block_list)
    for x,y in zip(block_list,block_list[1:]):
        actors.append(rope(x,y,Ast=10))
    actors.append(rope(a,block_list[0],Ast=10))
    actors.append(rope(b,block_list[-1],Ast=10))
    actors.extend((a,b))
    while True:
        newlife(flips=1)
def color_experiment():
    global a
    a=text(Sx=0,drag=True,fixed=[None,height/6])
    e=block(Sx=0,drag=True,fixed=[None,height/6])
    b=block(Sx=0,drag=True,fixed=[None,height/3])
    c=block(Sx=0,drag=True,fixed=[None,height/2])
    d=block(Sx=0,Sy=height/2+50,
                        Lx=width-10,Ly=height/2-50,drag=True)
    
    while True:
        for x in a,b,c,e:
            x.__move__()
            x.Sx=max(min(x.Sx,255),0)
            x.__show__(screen)
        d.color=a.Sx,b.Sx,c.Sx
        screen+d
        newlife()
        
def wave_show():
    global numpy,pyaudio,p
    import pyaudio
    p=pyaudio.PyAudio()
    my_fpb=50
    my_rate=3000
    #一个数据16bit 2B
    #2个ascii字符 4个16进制数
    #在[-256,32768]之间
    import struct
    import numpy
    print('successfully import')
    global Xin,MAXlist,MINlist
    MAXlist=numpy.zeros(
        width,dtype=numpy.int16)
    MINlist=numpy.zeros(
        width,dtype=numpy.int16)
    MAXpic,MINpic=(dots(MAXlist,Sy=height/2),
                   dots(MINlist,Sy=height/2))
    pen_point=0
    
    river=p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=my_rate,
        input=True,
        frames_per_buffer=my_fpb)
    while True:
        newlife()
        Xin=river.read(my_fpb)
##        Xin=struct.unpack('h',Xin)[0]
##        Xin=Xin>>7
##        Xlist[pen_point]=Xin
        Xin=numpy.frombuffer(
            Xin, dtype=numpy.int16)
        x,y=max(Xin)>>7,min(Xin)>>7
        MAXlist[pen_point]=x
        MINlist[pen_point]=y
        if x>250 or y<-250:
            print(x,y)
        screen+MAXpic+MINpic+\
            dots(Xin>>7,Sy=height/2)
        pen_point+=1
        pen_point%=width

