import numpy as np
fps = 44100 # Hz
f = 440 # Hz
second = 5 #s
myarray = np.arange(fps*second)
myarray = np.sin(2*np.pi*  f/fps * myarray)
#myarray属于[-1,1] 超过这个的数都会被强行转化

#这是为了消除开始和结尾的噪音
myarray[:4410]*=np.linspace(0,1,4410)
myarray[-4410:]*=np.linspace(1,0,4410)

import sounddevice as sd
sd.play(myarray, fps)


