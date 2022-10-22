
from time import time,sleep


print('欢迎使用节拍器！')
bpm=int(input('请输入你想要的拍速 按照bpm'))
bps=bpm/60
beats=int(input('输入请输入每小节节拍数'))

group_head=time()
while True:
    dt=time()-group_head
    d_beat=dt*bps
    if d_beat>beats:
        group_head=time()
    else:
        print(round(d_beat+1,2))
        sleep(0.001)
