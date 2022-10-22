import tkinter as tk
root=tk.Tk() #创建一个tk窗口
#创建窗口和输入栏
#自动调节大小：长30字高14行
root.title("David Demo")
text=tk.Text(root,width=40,height=14,
             font=("微软雅黑",22))
text.pack()
#  写入初始字符
text.insert(tk.INSERT,
'''欢迎！这是一个帮助你使用cmd的小工具
''')
#创建顶部菜单
menu=tk.Menu(root)
# 显示菜单
root.config(menu=menu)


#接下来绑定函数和按钮
menu.add_command(label="Run",
                 command=lambda x:None)
import subprocess
cmd=subprocess.Popen('cmd.exe',
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE)

#当按下换行就把这一行交给cmd,
def callback(event):
    res,err=cmd.communicate(b"echo hello")
    text.insert(tk.INSERT,res)
    #Return就表示换行
text.bind("<Key-Return>",callback)
#开始程序
root.mainloop()
