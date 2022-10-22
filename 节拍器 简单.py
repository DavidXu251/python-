
input('开始-->')
import time

last=time.time()
delta=[]
while True:
    input()
    delta.append(time.time()-last)
    #print(round(delta[-1], 3))
    #print(round(60/(time.time()-last), 1) )
    last=time.time()
    
    
    ave_time=sum(delta)/len(delta)
    ave_speed=60/ave_time
    print( round(ave_speed, 1))
    


speed=70
for i in range(999):
    time.sleep(70/60)
    print(i, end=' ')
