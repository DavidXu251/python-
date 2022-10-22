
import numpy as np
import matplotlib.pyplot as plt
from numpy import sqrt,sin,cos,log

x=(-1-sqrt(5))/4
lst=[np.linspace(x,x+0.5,4)]

#f=lambda x: -sqrt((x+1)/2)
f=lambda x: 2*x**2-1

for i in range(10):
    lst.append(f(lst[-1]))

print(lst[-1][-1], f(lst[-1][-1]) )
lst=np.array(lst)
plt.plot(lst)
plt.show()
