#一个物体受力
#M P不变, 求V
#P=Fv   F=P/v
#F合=P/v-f~a
#v'=P/v-f
#就是（v的导数）正比于1/v-定
P=20
a=v=s=0.1
f=1
delta_t=0.003
import numpy as np
v_rec=np.zeros((20000,))
s_rec=v_rec*0
for _ in range(len(v_rec)):
    a=(P/v-f)/1
    v=v+a*delta_t
    s=s+v*delta_t
    v_rec[_],s_rec[_]=v,s
print('s=',s,'v=',v)
import matplotlib.pyplot as plt
plt.subplot(2,1,1)
plt.scatter(range(0,len(s_rec)),s_rec)
plt.subplot(2,1,2)
plt.scatter(range(0,len(v_rec)),v_rec)
plt.show()
'''
import pygame
pygame.init()
screen=pygame.display.set_mode((500,400))
screen.fill((255,255,255))
for i,v in enumerate(v_rec):
    screen.set_at((i,30),(0,0,00))
pygame.display.flip()
'''
