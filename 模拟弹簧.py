
import numpy as np
import matplotlib.pyplot as plt

dt=0.01
duration=5

x=1
v=0
m=1
G=10*m

k=100
h=0.5

x_data=[]
F_data=[]
for _ in range(int(duration/dt)):
    F=-G + k*max(h-x,0)
    a=F/m
    v+=a*dt
    x+=v*dt
    x_data.append(x)
    F_data.append(F)

plt.plot(x_data)
plt.plot(F_data)
plt.show()
