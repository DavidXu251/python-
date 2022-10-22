import pygame;pygame.init()
screen1=pygame.display.set_mode((600,500))
def news(x,y,xl,yl,wid):
    pygame.draw.rect(screen1,(255,255,255),\
                  (x,y,xl,yl),wid)#矩形
    pygame.display.update()
def nextmove(a):
    b=a%4
    if b==1:return (5,0)
    if b==2:return (0,-5)
    if b==3:return (-5,0)
    if b==0:return (0,5)
def isdry(x):
    a=2
    while a<=x/2:
        if x%a==0:
            return False
        a+=1
    return True
ll=[None,1,0,0]
def nextt(move):
    move[1]+=1
    maxx=(move[0]+1)/2
    maxx=int(maxx)
    if move[1]>=maxx:
        move[0]+=1;move[1]=1
    return move
def sumdry():
    a=1
    summ=0
    drylist=[]
    while True:
        a+=1
        #print('Now a is ',a)
        if isdry(a):
            #drylist+=[a]
            summ+=1/a/a
            print(a,summ)
            #print('A is dry.All a till now is',drylist,'Summ is',summ)
            #input('开始')

x=1;a=300;b=250;move=[1,1]
while True:
    x+=1;print('x is',x)
    if isdry(x):
        news(a,b,5,5,0)
        print(x,'是素数',a,b)
    #else:news(a,b,5,5,1)
    move=nextt(move)
    speed=nextmove(move[0])
    a+=speed[0];b+=speed[1]
