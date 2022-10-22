import numpy as np
import matplotlib.pyplot as plt

x_data=np.arange(0,10, 0.002,float)
data=x_data*0

for omiga in range(1,500):
    data+=np.sin(omiga*x_data)

plt.plot(data)
plt.show()
