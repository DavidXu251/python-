
class Chord:
    def __init__(self,root,ch_type='maj'):
        if ch_type=='maj':
            self.notes=[root,root+4,root+7]
        elif ch_type=='min':
            self.notes=[root,root+3,root+7]
        else:
            print('unknown chord type:',ch_type)
    def match_extent(self,lst):
        ans=0
        for note in self.notes:
            ans+=min( sum(lst[note::12]), 1)
        return ans

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

width,height=600,400
screen=pygame.display.set_mode(
    (width,height),
    pygame.RESIZABLE)

import numpy as np
import matplotlib.pyplot as plt

print(sys.path[0])
folder='10178首游戏音乐\\'
print(folder)

file_names=os.listdir(folder)
random.shuffle(file_names)
for name in file_names:
    print(name)
    midi_file=mido.MidiFile(folder+name)

    music.load(folder+name)
    music.set_volume(0.3)
    music.play()

    lst=np.zeros((128,))
    next_play_time=time.time()
    for note in midi_file:
        next_play_time+=note.time
        time.sleep(max(
            next_play_time-time.time(),
            0))
        if note.type=='note_on':
            screen.fill((255,255,255))
            if note.velocity==0:
                lst[note.note]=0
            else:
                lst[note.note]=1
            chord_vals=np.zeros((9,))
            chords=[
                Chord(0),
                Chord(5),
                Chord(7),

                Chord(0,'min'),
                Chord(5,'min'),
                Chord(7,'min'),
                ]
            for i,chord in enumerate(chords):
                x=i%3
                y=i//3
                val=chord.match_extent(lst)/10
                val=min(max(val,0),1)
                color=(int(0*val+255*(1-val)),
                           int(150*val+255*(1-val)),
                           int(150*val+255*(1-val))
                           )
                pygame.draw.rect(screen,
                    color,
                    pygame.Rect(
                        x*width//3, y*height//3,
                        width//3-1, height//3-1),
                    0
                    )
            
            for event in pygame.event.get():
                if event.type==pygame.VIDEORESIZE:
                    width,height=event.size
                    screen = pygame.display.set_mode(
                        (width, height), pygame.RESIZABLE)
            pygame.display.flip()
    
    music.fadeout(1000)
    music.stop()


    

