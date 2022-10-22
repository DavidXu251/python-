import numpy as np
import numba as nb
import time
import wave
#@nb.jit(cache=True)
def doing(S,V,A,f,record,Vr):
    for i in range(100):
        S+=V
        #V-=S/200
        V=V*(100-f)
        #average=(S[0]-S[1])/2
        #S[0:2]+=(average-S[0:2])/20
        record[i]=S
        #Vr[i]=average
    return S,V,A,f,record,Vr
for _ in [0]:
    max_num=3
    S=np.zeros((max_num,), dtype='float')
    V=S*0
    V[0]=1
    A=S*0+1
    A[0:3]=1,1,1
    f=S*0+0.01
    alive=np.array(V,dtype='bool')


record=np.ndarray((10**6,),dtype='float')
Vr=record*0




start=time.time()
##S,V,A,f,record,Vr=doing(
##    S,V,A,f,record,Vr)
S,V,A,f,record,Vr=doing(
    0.,1,0,0,record,Vr)
end=time.time()
during=end-start
during=max(0.001,during)
print(f'用时{during}秒')
print(f'显示了10**6次')
print(f'帧数{10**6/during} ')
print('最大声音:', max(record))

f=wave.open('my_sound.wav','wb')
f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(30000)#60f/round
f.writeframes(record.tostring())






import matplotlib.pyplot as plt
showL=7000


plt.plot(np.arange(0,showL),record[:showL],
              color='blue',label='S')
plt.plot(np.arange(0,showL),Vr[:showL],
         color='orange',label='V')
plt.show()
