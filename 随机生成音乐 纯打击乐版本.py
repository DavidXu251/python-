

import mido
from mido import Message
import random

mid = mido.MidiFile()
track = mido.MidiTrack(channel=10)
mid.tracks.append(track)
track.append(
        Message('program_change',
                channel=10, program=10, time=0))

for i in range(16):
        track.append(
            Message('note_on', note=39,
                    velocity=64,
                    time=600))

track.append(
            Message('note_on', note=0,
                    velocity=0,
                    time=800))

mid.save('new_song.mid')

import pygame
pygame.mixer.init()
music=pygame.mixer.music
music.load('new_song.mid')
music.set_volume(0.5)
music.play()


