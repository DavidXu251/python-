import numpy as np
from matplotlib import pyplot as plt
x=np.linspace(0,100,50)
y=np.sin(x)
x1=np.linspace(0,100,300)
y1=np.sin(x1)

plt.subplot(2,1,1)#第一个分支'plot'
plt.title('sinx 50 points')
plt.xlabel('name of x')
plt.ylabel('name of y')
plt.plot(x,y)

plt.subplot(2,1,2)#第二个分支'plot'
plt.title('sinx 200 points')
___=plt.plot(x1,y1)

plt.show()
print(___)
