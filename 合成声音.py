import numpy as np
import matplotlib.pyplot as plt

class node:
    def __init__(self,s=0.,v=1.,k=0.01,f=1.):
        self.s=s
        self.v=v
        self.k=k
        self.f=f
    def move(self)->float:
        self.s+=self.v
        self.v-=self.k*self.s
        self.v*=self.f
        return self.s
#C4=261.626Hz, 44100/261.626=168.56个样本
rope=[node(s=1,v=0,k=0),
    node(s=0,v=3,k=0.0016),
      node(s=0,v=0,k=0.0016*0.666**2),
      
            ]
      #node(s=0,v=-2,k=0.0015*(1.04)**2),
k_between=0.0001

sound=np.zeros((44100*3,),  dtype="float64")
for i in range(len(sound)):
    sound[i]=   sum((x.move() for x in rope))
    for a,b in zip(rope,rope[1:]):
        delta=a.s-b.s
        a.v-=delta*k_between
        b.v+=delta*k_between
#这时sound是一个由响变轻的声音
#时长1秒，在开始会有爆炸声




#1 这是为了防止爆炸声,
sound[:4410]*=np.linspace(0,1,4410)**2
sound[-4410:]*=np.linspace(1,0,4410)**2

sound=np.hstack([    np.zeros((4410,)),
    sound,np.zeros((8820,))    ])

#2 调整声音，将最大值固定在1
s_max=max(max(sound),-min(sound))
sound*=(0.5/s_max)

#3 重复声音2遍
sound=np.hstack([sound]*2)


#打开wav文件
import wave
file=wave.open("sound.wav",'wb')
file.setparams(
    (1, 2, 44100, None, 'NONE', 'Tsinghua'))
#(声道，一个数据几字节，一秒几个数据，
#comptype, compname)

# .wav 文件接收的是int8 int16
#最大最小是 +-128 +-30000
sound=sound*(20_000/max(sound))
#sound+=20_000
sound=np.int16(sound)
file.writeframes(sound)
file.close()

def play(sound):
    #安全地播放声音
    sound=np.float64(sound)
    #1 这是为了防止爆炸声,
    sound[:4410]*=np.linspace(0,1,4410)**2
    sound[-4410:]*=np.linspace(1,0,4410)**2

    sound=np.hstack([    np.zeros((4410,)),
        sound,np.zeros((8820,))    ])

    #2 调整声音，将最大值固定在1
    s_max=max(max(sound),-min(sound))
    sound*=(0.5/s_max)
    #检测噪音
    Vy=[right-left for left,right
        in zip(sound[:-1],sound[1:])]
    Ay=[right-left for left,right
        in zip(Vy[:-1],Vy[1:])]
    maxS=max(max(sound),-min(sound))
    maxV=max(max(Vy),-min(Vy))
    maxA=max(max(Ay),-min(Ay))
    #decide to play the sound
    #   depending on our maxS maxV maxA
    if maxS>0.9:
        print("maxS太大",maxS)
    elif maxV>0.03:
        print("maxV太大",maxV)
    elif maxA>0.001:
        print("maxA太大",maxA)
    else:
        print("安全播放")
        #播放声音
        import sounddevice as sd
        sd.wait()
        sd.play(sound,44100)

def mat(sound):
    #画图
    import matplotlib.pyplot as plt
    plt.scatter(y=sound,x=np.arange(len(sound)) ,)
    plt.xlim((0,400))#设置坐标轴取值范围
    plt.ylim((-1,1))
    plt.show()
def plot(sound):
    width,height=500,400
    sound//=max(sound)//(height//2)#固定最大值
    Sx=8000
    import pygame
    pygame.init()
    screen = pygame.display.set_mode(
        (width,height))
    while True:
        for eve in  pygame.event.get():
            if eve.type==12:#退出键
                pygame.quit()
                return None
            if eve.type==2:#鼠标按下
                if eve.unicode=='d':
                    Sx+=200
                    print('Sx=',Sx)
                if eve.unicode=='a':
                    Sx-=200
                    print('Sx=',Sx)
        screen.fill((0,0,0))
        for x,y in enumerate(sound[Sx:Sx+width]):
            screen.set_at((int(x),y+height//2),(255,255,255))
        pygame.display.flip()
play(sound)
plot(sound)
