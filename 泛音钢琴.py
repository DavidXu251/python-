


fps=60
rate=44100


import time
def sleep_until(t):
    to_sleep=t-time.time()
    if to_sleep>0:
        time.sleep(to_sleep)
    else:
        pass

import sounddevice as sd
stream=sd.OutputStream(
        samplerate=rate,
        channels=1,
        )
stream.start()
next_frame_time=time.time()

import numpy as np
old_loudness=np.zeros((84,))
loudness=np.zeros((84,))
sin_lst=[]
for note in range


import pygame
pygame.init()
width,height=600,500
screen=pygame.display.set_mode(
    (width,height))























