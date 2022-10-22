from random import randint as r
a=[[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]

def new(a):
    a[r(0,3)][r(0,3)]=r(1,2)
    return a
a=new(a)
