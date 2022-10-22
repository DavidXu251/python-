
import mido
import numpy as np
import time

import random
import sys
import os

import pygame
pygame.init()
pygame.mixer.init()
music=pygame.mixer.music

width,height=1024,400
screen=pygame.display.set_mode(
    (width,height))

import numpy as np
import matplotlib.pyplot as plt

#读取midi乐器对照表
import codecs
midi_no_lst=codecs.open('midi乐器对照表.txt',
    encoding='utf-8').read().split('\r\n')
midi_no_dict=dict()
for line in midi_no_lst:
    words=line.strip().split(' ')
    if len(words)>=2:
        if words[0].isdigit():
            midi_no_dict[int(words[0])]=' '.join(words[1:])
print(sys.path[0])
folder='10178首游戏音乐\\'
print(folder)

file_names=os.listdir(folder)
random.shuffle(file_names)
for name in file_names:
    print()
    print(name)
    midi_file=mido.MidiFile(folder+name)
    lst=np.zeros((128,))

    music.load(folder+name)
    music.set_volume(0.3)
    next_play_time=time.time()
    music.play()


    bad_channel=[]
    ch_to_pro={}
    for note in midi_file:
        next_play_time+=note.time
        time.sleep(max(
            next_play_time-time.time(),
            0))
        
        if note.type=='program_change':
            print(note.channel,'->', note.program, 
                midi_no_dict.get(note.program,'未知'))

            ch_to_pro[note.channel]=note.program
        elif note.type=='note_on':
            if note.channel==10:
                note.note=0
                note.velocity=10
            #                    48->定音鼓 56->乐队打击乐
            elif ch_to_pro.get(note.channel,1) in (48,56):
                note.note=0
                note.velocity=10
                #print(ch_to_pro[note.channel])
            delta=note.velocity/10
            lst[note.note]+=delta
            if np.max(lst)>height:
                lst/=2
            screen.fill((255,255,255))
            #lst_by_scale=lst/np.sum(lst)*height*3
            x=0
            for velocity in lst:
                velocity=max(int(velocity),0)
                pygame.draw.rect(screen,
                    pygame.Color(0,0,0),
                    pygame.Rect(x,height-velocity,
                                8,velocity),
                    0
                    )
                x+=8
            for event in pygame.event.get():
                if event.type==12:
                    pygame.quit()
                    exit()
            pygame.display.flip()
        
    
    music.fadeout(1000)
    music.stop()


    
