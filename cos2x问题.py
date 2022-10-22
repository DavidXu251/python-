











import numpy as np
import matplotlib.pyplot as plt

from math import pi

size=2**11
lst=list(range(0,size))

for n in range(0,10):
    interval=size/4/(2**n)
    lst=[x for x in lst if (x//interval)%4 in (1,2)]
    plt.scatter(np.array(lst), np.array(lst)*0+n )
print(lst)
plt.scatter(0,0)
plt.scatter(size,0)
plt.show()



assert False







x=np.linspace(-pi, pi, 500)

for n in range(0,12):
    angle=x[ np.where( np.cos(2**n*x)<0) ]
    
    plt.scatter(
        (n+1)*np.cos(angle),
        (n+1)*np.sin(angle)
                )

plt.show()
