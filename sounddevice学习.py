
import numpy as np
from math import pi
import sounddevice as sd

def fade(y, fade_t=0.2, empty_t=0.1, lim=0.3):
    y_min=np.max(y)
    y_max=np.min(y)
    y=y.copy()
    y-=(y_min+y_max)/2
    y/=(y_max-y_min)/2
    y*=lim
    
    frames=int(fps*fade_t)
    y[:frames]*=np.linspace(0,1,frames)**2
    y[-frames:]*=np.linspace(1,0,frames)**2

    zeros=np.zeros( [int(fps*empty_t)] )
    y=np.insert(y,0, zeros)
    y=np.append(y,zeros)
    return y


#sample rate
fps=44100
freq=522
x=np.linspace(0,3,fps*3)
y=(0
   +np.sin(x*2*pi*freq*0.5)
    +np.sin(x*2*pi*freq*1)
    +np.sin(x*2*pi*freq*2)
    +np.sin(x*2*pi*freq*3)
    +np.sin(x*2*pi*freq*4)
   +np.sin(x*2*pi*freq*5)
   #+np.sin(x*2*pi*freq*8)
    )
y=fade(y)

if 0:
    import matplotlib.pyplot as plt
    plt.plot(y)
    plt.show()
else:
    sd.play(y)
    sd.wait()





