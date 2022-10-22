
import os
os.system('cmd')

import subprocess as sp
import threading

def setup(command='cmd'):
    global cmd,p
    cmd=command
    p=sp.Popen(cmd,
                    shell=True,
                    stdin=-1,
                    stdout=-1,
                    )

gbk='gbk'

out_buffer=''
out_byte_buffer=b''
def callback_main():
    global p
    while True:
        out_byte_buffer+=p.stdout.read()
        try:
            out_buffer+=out_byte_buffer.decode(gbk)
            out_byte_buffer=b''
        except UnicodeDecodeError:
            pass












import tkinter as tk
root=tk.Tk()

text=tk.Text(root,
             font=('微软雅黑',20),
             width=40,
             height=15,
             )
text.pack()

import subprocess as sp
import threading
import time

gbk='gbk'
cmd='C:/Apps/Python38/python.exe'
cmd='cmd\n'
print('running', cmd)


p=sp.Popen(cmd,
                shell=True,
                stdin=-1,
                stdout=-1,
                )
def key_press(event):
    char=chr(event.keycode)
    print('have',char)
    global p
    p.stdin.write(char.encode(gbk))
    
text.bind('<KeyPress>', key_press)


last=b''
while True:
    time.sleep(0.1)
    p.stdin.write('\n'.encode(gbk))
    got=p.stdout.read(1)

    last+=got  #由于read(1)返回的是一个字节，而不是一个gbk字符
    #因此输出中文会有问题，我们要把got缓存到last中，等到last成为合法的字符再发送
    try:
        char=last.decode(gbk)
        
        print(char , end='')
        text.insert(tk.INSERT,char)
        root.update()
        last=b''
    except UnicodeDecodeError:
        pass



tk.mainloop()
    




    
