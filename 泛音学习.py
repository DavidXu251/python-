

import numpy as np

import sounddevice as sd
rate=48000
stream=sd.InputStream(
        samplerate=rate,
        channels=2,
        )
stream.start()


import pygame
pygame.init()
width,height=600,600
screen=pygame.display.set_mode((
    width,height))
black=(0,0,0)
gray=(250,250,250)
white=(255,255,255)

def plot(data,Oy=height/2,color=black):
    data=Oy-data
    data=data.astype(int)
    pygame.draw.lines(screen,
        black,False,
        list(enumerate(data)),
        1)

full_data=np.zeros((width*3,))
place=0
while True:
    data2d, err =stream.read(width)
    data=data2d[::, 0]
    
    full_data[place:place+width]=data
    place=(place+width)%width
    
    screen.fill(white)

    plot(data*200,Oy=100,color=gray)
    plot(np.abs(np.fft.fft(full_data))*1,
         Oy=300,color=gray)
    '''
    for freq in [1,2,3,4,5]:
        loud=abs(np.complex(
            np.sin()*full_data,np.cos(full_data
            ))
            '''
    

    
    
    pygame.event.get()
    pygame.display.flip()








