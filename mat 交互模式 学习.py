import numpy as np
import matplotlib.pyplot as plt
print('成功导入')
Xlist=np.linspace(0,3,100)
for i in np.linspace(0,3,100):
    print(i)
    Ylist=i*(Xlist-i)**2+i
    plt.plot(Xlist,Ylist)
    plt.pause(0.01)
