
import sympy as sy
from sympy.abc import a,b,c,d,x,y

#x**2/a**2 + y**2/b**2 == 1
#A(c,d)
B=sy.solve([
    x**2/a**2 + y**2/b**2 - 1,
    x-c
],x,y)
B.remove((c,d))
B=B[0]
print(B)
