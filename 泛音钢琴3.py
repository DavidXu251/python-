
import sounddevice as sd
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import time

class Piano:
    def __init__(self):
        self.rate=48000
        self.chunk_size=48000//240
        self.chunk_time=self.chunk_size/self.rate
        self.base_freq=55* 2**(3/12) /4
        print(self.base_freq)
        self.stream=sd.OutputStream(
                samplerate=self.rate,
                channels=1,
                )
        self.stream.start()
        

        self.old_keys=np.zeros((88,))
        self.time_since_start=0
        self.start_time=time.time()
        
    def __del__(self):
        self.write(np.zeros(88,))
        time.sleep(self.chunk_time*1.5)
        self.stream.close()
        
    def write(self, keys):
        old_keys=self.old_keys
        if len(old_keys)!=len(keys):
            print('keys length not matched',
                  len(old_keys), len(keys))
        
        sound=np.zeros((self.chunk_size,))
        t=np.linspace(
            self.time_since_start,
            self.time_since_start + self.chunk_time,
            self.chunk_size
            )
        for (note,(old_amp,amp)) in enumerate(zip(
                self.old_keys,keys)):
            if old_amp<0.001 and amp<0.001:
                continue
            freq= self.base_freq* 2**(note/12)
            #phase->相位
            this_sound=np.sin(2*pi*t*freq)
            this_sound*=np.linspace(
                old_amp, amp, self.chunk_size)
            sound+=this_sound
        sound/=len(keys)
        #plt.plot(sound)
        #plt.pause(0.01)
        if np.max(sound)>1:
            print('sound too loud')
            exit()
        plt.cla()
        plt.plot(sound)
        plt.pause(0.0001)
        time.sleep(
            max(
            self.start_time+self.time_since_start
            -time.time()-self.chunk_time,
            0)
        )
        self.stream.write(sound.astype('float32'))
        self.old_keys=keys.copy()
        self.time_since_start+=self.chunk_time
        
def shift(arr, count):
    new_arr=arr*0
    new_arr[count:]=arr[:-count]
    return new_arr

piano=Piano()
keys=np.zeros((88,))

import mido
device=mido.open_input()
keys=np.zeros((88,))
while True:
    msg=device.poll()
    if msg is not None:
        if msg.velocity!=0:
            keys[msg.note]=1
        else:
            keys[msg.note]=0
    
    keys_spread=(
        keys
        +shift(keys,12)
        +shift(keys,12+7)
        +shift(keys,24)
        )/4
    piano.write(keys_spread)

del piano













