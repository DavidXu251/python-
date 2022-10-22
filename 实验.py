def getx():
    global x
    x0=x
    x+=1
    return x0
def setx(val):
    global x
    x==val
def delx():
    pass
x=property(getx,setx,delx)

