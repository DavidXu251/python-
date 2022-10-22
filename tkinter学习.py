import tkinter as tk
root=tk.Tk() #创建一个tk窗口
#创建窗口和输入栏
#自动调节大小：长30字高14行
root.title("David Demo")
text=tk.Text(root,width=40,height=14,
             font=("微软雅黑",22))
text.pack()
#写入初始字符
text.insert(tk.INSERT,
'''package main
import "fmt"

func main(){
    fmt.Println("Hello!")
}
''')
#创建顶部菜单
menu=tk.Menu(root)
#显示菜单
root.config(menu=menu)
#处理cmd命令
import subprocess as sp
process = subprocess.Popen("C:\\",creationflags=subprocess.CREATE_NEW_CONSOLE)
def run():
    global text,process
    with open("experiment.go","w") as gofile:
        gofile.write(text.get('0.0','end'))
    print(process.stdout.read().decode(encoding="gbk"))
menu.add_command(label="Run",
                 command=run)


#开始程序
root.mainloop()
