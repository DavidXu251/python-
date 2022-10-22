
import numpy as np
import matplotlib.pyplot as plt

def f1():
    '''计算x范围内，每个数到0的汉明距离'''
    x=list(range(100))
    y=[bin(i).count('1')+1 for i in x]
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.show()

def haming(x,y,base=2):
    res=0
    while not (x==0 and y==0):
        x, rem_x=divmod(x,base)
        y, rem_y=divmod(y,base)
        res+=abs(rem_x - rem_y)
    return res

def f2():
    size=128
    data=np.zeros((size,size))
    for y in range(size):
        for x in range(size):
            #data[y,x]=haming(x,y, base=2)
            #data[y,x]=haming(x,y+x, base=2)
            #data[y,x]=abs(x-y)
            #data[y,x]=x^y
    plt.imshow(data, cmap='gray')
    plt.show()
    
    from PIL import Image
    data=(data/np.amax(data)*255).astype('uint8')
    im=Image.fromarray(data)
    im=im.resize((size*100, size*100),
                 Image.NEAREST)
    print(im.size)
    im.save('汉明距离.png')

    import os
    #os.system('汉明距离.png')


f2()







    
