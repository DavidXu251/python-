

import numpy as np
from math import factorial
import matplotlib.pyplot as plt

x=1
lst=[]
for i in range(1,366):
    x*=(365-i+1)/365
    lst.append(1-x)

plt.plot(lst)
plt.show()
