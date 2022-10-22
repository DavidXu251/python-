


import mido
import os
import random

import numpy as np
import pandas as pd
import pickle



folder='10178首游戏音乐\\'
file_names=os.listdir(folder)
random.shuffle(file_names)

output_file=open('音乐数据bin版.bin', 'wb')


print(len(file_names))

file_count=0
for name in file_names:
    
    file_count+=1
    if file_count%10==0:
        print(file_count)
    

    if not name.endswith('.mid'):
        continue
    
    midi_file=mido.MidiFile(folder+name)
    
    keys=[x for x in midi_file
          if x.type=='note_on']
    keys2=[]
    pressed_keys={}
    timing=0
    
    for key in keys:
        timing+=key.time
        if key.velocity>0:
            pressed_keys[(key.channel, key.note)]=timing
        elif key.velocity==0:
            try:
                start_time = pressed_keys.pop(
                    (key.channel,key.note))
            except: continue
            delta_time = timing-start_time
            keys2.append((key.note, start_time, delta_time))
    keys2=np.array(keys2)
    output_file.write(keys2.tobytes())
    
    
output_file.close()

    
        

        




    
