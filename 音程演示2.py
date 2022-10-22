
import numpy as np
from numpy import sin,cos,pi

data=np.zeros((10000,))
x=np.linspace(0,2*pi,10000)
data+=sin(10*x)*100
data+=sin(11.2345*x)*100
print(sin(100*x))
import matplotlib.pyplot as plt
plt.plot(data)
plt.show()
