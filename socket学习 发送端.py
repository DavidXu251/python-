
import numpy as np
import time
import socket               # 导入 socket 模块

print(socket.gethostbyname(
    socket.gethostname()))

host = socket.gethostname() # 获取本地主机名
port = 1               # 设置端口
print(host)

'''
def task():
    while True:
        s2=socket.socket()
        s2.connect((host,port))
        print(s2.recv(1024))
thread=threading.Thread(target=task)
thread.start()
'''

size=1024*1024*100
number=100
#生成随机bytes数据
data=np.random.randint(0,255,
        size=size, dtype='uint8').tobytes()

s = socket.socket()         # 创建 socket 对象
s.bind((host, port))        # 绑定端口

s.listen(5)                 # 等待客户端连接

def task2():
    c,addr = s.accept()     # 建立客户端连接
    c.send(data)
    #c.send(bytes(str(time.time()),encoding='ascii'))
    c.close()                # 关闭连接

for i in range(number):
    start=time.time()
    task2()
    end=time.time()
    t=max(end-start,0.001)
    print('time=',round(t,2))
    print('speed=', round(size/1024/1024/t,2),
          'MB/s')









