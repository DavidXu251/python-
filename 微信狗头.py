
from math import cos
import numpy as np
from numpy import pi

for i in np.linspace(0,4*pi,40):
    x=int(20*cos(i)+20)
    print(x*' '+3*'/大哭')

exit()

for _ in range(10):
    for i in [0,1,2,3,4,5,6,7,6,5,4,3,2,1]:
        print(5*i*' '+3*'/微笑')
        
input()