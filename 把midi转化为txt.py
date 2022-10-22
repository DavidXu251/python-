


import sys,os

import mido
import codecs


print(sys.path[0])
folder=sys.path[0]+'\\10178首游戏音乐\\'
print(folder)

file_names=os.listdir(folder)

txt_file=codecs.open(
    file_names[0]+'.txt', 'w', 'utf-8')

for file_name in os.listdir(folder):
    midi_file=mido.MidiFile(folder+file_name)
    input(file_name)
    for track in midi_file.tracks:
        txt_file.write('\n')
        for msg in track:
            if msg.type=='note_on':
                if msg.velocity!=0:
                    #每个unicode字符有3个字节
                    #需要在0x110000以下
                    #即小于等于0010ffff
                    txt_file.write(chr(
                        msg.note*0x100
                      +msg.time))

txt_file.close()
                    






        

