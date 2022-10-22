
import mido
from mido import Message
import random

mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)
track.append(
        Message('program_change', program=1, time=0))

root=60
for i in range(16):
    root=root+random.choice([0,-5,5,-7,7])
    if root>60+24:
        root-=12
    elif root<60-24:
        root+=12
    
    chord=random.choice([
        [-12,0,4,7],
        [-12,0,4,7],
        [-12,0,2,7],
        [-12,0,5,7],
        ])
    chord=[i+root for i in chord]
    timing=800
    print(chord)
    for i in chord:
        track.append(
            Message('note_on', note=i, velocity=64,
                    time=timing//4))

track.append(
            Message('note_on', note=i, velocity=64,
                    time=800))

mid.save('new_song.mid')

import pygame
pygame.mixer.init()
music=pygame.mixer.music
music.load('new_song.mid')
music.set_volume(0.5)
music.play()


