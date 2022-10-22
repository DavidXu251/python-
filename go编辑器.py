
import threading
import time
def later(func, timing, para=[]):
    def func1():
        time.sleep(timing)
        func(*para)
    threading.Thread(target=func1).start()

import tkinter as tk
import os

#读取文件
file_path=os.getcwd()+'\\'+'no name.go'
if not os.path.exists(file_path):
    file=open(file_path)
    file.write(    '''package main
    import "fmt"
    func main(){
        fmt.Println("Hello!")
    }
    ''')
    file.close()

root=tk.Tk()
root.title("editing"+file_path)

#这里要提高分辨率
#各个电脑屏幕像素的密度，都不一样
#如果一个程序只为500*400像素的窗口设计
#那么像素多的屏幕上，这个窗口就显得很小
#为了解决这个问题，操作系统
#       都会会设置一个"屏幕缩放"
#在程序看来是1个像素，但是在实际画图的时候
#       操作系统 会把它 当作4个 9个 16个像素去渲染
#       我的电脑就是放大200% 这个在windows设置里可以改
#这样就可以在保持高分辨率的前提下 放大窗口
#然而我们用的tkinter没有使用系统自带的画图功能
#这就导致操作系统仅仅放大了图像
#       而文字的分辨率却没有对应地提高
#       所以里面的字看起来就很模糊
#所以我们要告诉系统，干脆不要帮我们缩放了
#我们转而使用tkinter的缩放功能，达到一样的效果

#这里使用的windll 没有支持macos linux
import ctypes
#在windows中能正确处理dpi的程序
#叫做high dpi aware
#告诉windows我们是一个high dpi aware的程序
ctypes.windll.shcore.SetProcessDpiAwareness(True)
#获取屏幕设置的 缩放因子 我的是200 表示缩放200%
scale=ctypes.windll.shcore.GetScaleFactorForDevice(0)
print('缩放比例：',scale)
#设置tkinter的程序缩放
root.tk.call('tk', 'scaling', scale/75)

text=tk.Text(root,
             font=("微软雅黑",22),
             width=40,
             height=14,
             undo=True
             )
text.pack()
text.insert('insert', open(file_path, 'r').read())


def when_keypress(event):
    key=event.keysym
    def count_last_line_space():
        last_line=text.get('insert-1l linestart',
                               'insert-1l lineend')
        return len(last_line)-len(last_line.lstrip())
    
    def todo_now(key):
        if key=='F5':
            print('running')
            new_run_window()
        else:
            later(todo_later, 0.0001, [key])
    def todo_later(key):
        if key=='Tab':
            text.replace('insert-1c', 'insert',' '*4)
        elif key=='Return':
            text.insert('insert', ' '*count_last_line_space())
        elif key=='BackSpace':
            cursor_left=text.get('insert linestart', 'insert')
            if cursor_left.isspace():
                text.delete('insert linestart', 'insert')
                text.insert('insert', ' '*(len(cursor_left)//4*4) )
        else:
            print(key, end=' ')
    todo_now(key)
        
text.bind('<Any-KeyPress>',when_keypress)


def save():
    #1.0 means the first line
    string=text.get("1.0",tk.END)
    with open(file_path,'w') as file:
        file.write(string)
        file.close()
        print('file saved')

 
def new_run_window():
    save()
    run_root=tk.Tk()
    run_root.title("running"+file_path)
    text=tk.Text(run_root,width=40,height=14,
         font=("微软雅黑",22))
    text.pack()

    import subprocess as sp
    
    program_word=(
        'go run '+'"'+file_path+'"'
        )
    program=sp.Popen(
        program_word,
        shell=True,
        stdout=sp.PIPE,
        stderr=sp.PIPE,
        encoding='gbk',
        )
    text.insert('insert', 'running: '+program_word+'\n'*3)
    print('running: '+program_word+'\n'*3)
    
    def update():
        try:
            got=(
                program.stdout.read()
                +program.stderr.read()
                )
            text.insert('insert',got)
            #在60/1秒后再执行一次update()
            run_root.after(1000//60, update)
        except BaseException as error:
            print('err:', error)
    run_root.after(1000//60, update)





root.mainloop()
