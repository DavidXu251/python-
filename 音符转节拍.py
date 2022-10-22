
import time

import mido
midi_port=mido.open_input()

import pygame
pygame.init()
width,height=600,500
screen=pygame.display.set_mode((
    width,height))
white=255,255,255
black=0,0,0
gray=200,200,200
blue=150,150,255

def draw_if_wanted(x,y,wanted_note,size=30):
    global keys
    x=int(x)
    y=int(y)
    
    if wanted_note in keys:
        freq=2**(note/12)
        interval=1/freq*16
        if ((time.time()-keys[note])
            %interval)<interval/2:
            color=black
            global beats_sum
            beats_sum+=4
        else:
            color=gray
    else:
        color=white
    pygame.draw.rect(screen,color,
        (x,y,size-1,size-1),
        0)
    if wanted_note%12==0:
        pygame.draw.rect(screen,blue,
            (x,y,size-1,size-1),
            3)
        

keys=dict()
beats_sum_lst=[height//2]*width

while True:
    beats_sum=height//2
    time.sleep(1/240)
    screen.fill(gray)
    pygame.event.get()
    
    msg=midi_port.poll()
    if msg is not None:
        if msg.velocity!=0:
            keys[msg.note]=time.time()
        else:
            keys.pop(msg.note, None)

    for x in range(0,width,30):
        for y in range(0,height,30):
            note=round(x/30*4+y/30*7)+24
            draw_if_wanted(x,y,note)
            
    beats_sum_lst.pop(0)
    beats_sum_lst.append(beats_sum)
    pygame.draw.aalines(screen,black,False,
        list(zip(range(width),beats_sum_lst)),
        1)
    pygame.display.flip()



        


