
import time

import mido
device=mido.open_input()

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
        interval=1/freq
        if time.time()%interval<interval/2:
            color=black
        else:
            color=gray
    else:
        color=white
    pygame.draw.rect(screen,color,
        (x,y,size-1,size-1),
        0)
    if wanted_note==0:
        pygame.draw.rect(screen,blue,
            (x,y,size-1,size-1),
            3)

keys=dict()
keys_full=dict()


while True:
    time.sleep(1/120)
    screen.fill(gray)
    pygame.event.get()
    
    msg=device.poll()
    if msg is not None:
        if msg.velocity!=0:
            keys[msg.note%12]=msg.velocity
            keys_full[msg.note]=msg.velocity
        else:
            keys.pop(msg.note%12, None)
            keys_full.pop(msg.note, None)

    for note in range(36,50):
        draw_if_wanted(note*30,height/2-30,note)
    for x in range(0,width,30):
        y=height/2
        i=int(x/30-width/30/2)
        note=(i//2)*7+(i%2)*4
        draw_if_wanted(x,y,note)


    pygame.display.flip()



        
