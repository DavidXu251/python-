

import mido
import os
import random

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

folder='10178首游戏音乐\\'
file_names=os.listdir(folder)
random.shuffle(file_names)

count=0
table=np.zeros( (12,12) )
for name in file_names:
    try:
        midi_file=mido.MidiFile(folder+name)
    except: continue

    count+=1
    if count%10==0:
        print(count)
    if count%100==0:
        for i in range(12):
            table[i, i]=0
        print(table)
        table1=(table/np.max(table)*255).astype('uint8')
        (
            Image.fromarray(table1, 'L')
            .resize((480,480), Image.NEAREST)
            .save('统计图.png')
        )
        os.system('统计图.png')
    tone=0
    notes=[]
    msg_iter=iter(midi_file)
    while True:
        try:
            msg=next(msg_iter)
        except: break
        if msg.type=='key_signature':
            key=0
            tone_name=msg.key
            if 'm' in msg.key:
                tone_name=tone_name[:-1]
            if '#' in tone_name:
                tone=['C', 'C#', 'D', 'D#', 'E',
                      'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'
                      ].index(tone_name)
            elif tone_name=='Cb':
                tone=11
            else:
                tone=['C', 'Db', 'D', 'Eb', 'E',
                      'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B'
                      ].index(tone_name)
        elif msg.type=='note_on':
            if msg.velocity!=0 and msg.channel!=10:
                notes.append(
                    (msg.note-tone)%12
                    )
    for left,right in zip(notes[:-1], notes[1:]):
        table[left, right]+=1

    
        

        




    
