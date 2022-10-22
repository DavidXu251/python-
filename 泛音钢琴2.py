


fps=60
rate=44100


import time

import sounddevice as sd
stream=sd.OutputStream(
        samplerate=rate,
        channels=1,
        )
stream.start()
next_frame_time=time.time()

def sleep_until(t):
    to_sleep=t-time.time()
    if to_sleep>0:
        time.sleep(to_sleep)
    else:
        pass
def time_to_frame(t):
    global rate
    return int(t*rate)
def fade_in_out(sound):
    frame=len(sound)//20
    sound[:frame]*=np.linspace(0,1,frame)
    sound[-frame:]*=np.linspace(1,0,frame)
    return sound
def repeat(arr,count):
    new_arr=np.zeros((len(arr)*count,))
    for i in range(count):
        new_arr[len(arr)*i : len(arr)*(i+1)]=arr
    return new_arr
def make_sound(freq=440,timing=1,amp=0.3):
    cycle=int(timing/freq*rate)
    x=np.arange(0,cycle)
    sound=np.sin(x*2*pi/cycle)*amp
    sound=repeat(sound,int(freq*timing))
    sound=fade_in_out(sound)
    return sound

def add_sound(*args):
    #把几个声音数组相加 返回新的声音
    #直接使用 numpy自带的相加
    #几个声音的数组大小可以不同
    max_len=max([len(sound) for sound in args])
    new_sound=np.zeros((max_len,))
    for sound in args:
        new_sound[:len(sound)]+=sound
    #缩小倍数 取平均值
    new_sound/=len(args)
    return new_sound

import numpy as np
from numpy import pi
base=130*2
#钢琴
sound=add_sound(
    make_sound(base*1,2,0.4),
    make_sound(base*2,2,0.5),
    make_sound(base*3,2,0.1),
    make_sound(base*4,2,0.2),
    make_sound(base*5,2,0.1),
    make_sound(base*6,2,0.05),
    )
#大提琴

sound=add_sound(
    make_sound(base*1,2,0.5),
    make_sound(base*2,2,0.5),
    make_sound(base*2.9966,2,0.07),
    make_sound(base*4,2,0.15),
    make_sound(base*5.0,2,0.13),
    make_sound(base*5.9932,2,0.04),
    make_sound(base*7,2,0.10),
    )

import matplotlib.pyplot as plt
plt.ylim(-3,3)
plt.plot(sound)
plt.show()

if input('是否播放?')=='yes':
    if np.max(sound)<=1:
        stream.write(sound.astype('float32'))
    else:
        print('max(sound) 太大了')
        print(np.max(sound))
stream.write(np.zeros((rate,), dtype='float32') )

















