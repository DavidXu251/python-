#学习用python处理图片
import numpy as np #处理
import matplotlib.image as imger #读取
import matplotlib.pyplot as plt #显示
import numba as nb
def flip90_left(arr):
    arr=np.swapaxes(arr,0,1)
    arr=arr[::-1]
    return arr
def flip90_right(arr):
    arr=arr[::-1]
    arr=np.swapaxes(arr,0,1)
    return arr
@nb.jit()
def edge(pic,pic1):
    Ly=pic.shape[0]
    Lx=pic.shape[1]
    for x in range(Lx-2):
     for y in range(Ly-2):
      for col in range(3):
        here=(4*pic[y+1,x+1,col]
           -pic[y+2,x+1,col]
           -pic[y+0,x+1,col]
           -pic[y+1,x+2,col]
           -pic[y+1,x+0,col])
        pic1[y,x,col]=here
    pic1=pic1*100
    pic1=np.maximum(0.01,pic1)
    pic1=np.minimum(0.99,pic1)
    return pic1

for _ in ['读取图像']:
    pic=imger.imread('40.png',)
    #pic=flip90_right(pic)
    pic=np.array(pic,order='F')
    #pic现在是一个array了
     #只获取红色
    Ly,Lx,Lcol=pic.shape
for _ in ['画矩形']:
    pic[:200,:100]-=0.5
for _ in 0*['改成有趣的shape']:
    #(460, 819, 3)
    print(pic.shape)
    Lx-=1
    pic=pic[:460,:818,]
    pic=np.array(pic)
    #pic.shape=(Ly*2,Lx//2,3)
    #pic.shape=(Ly//2,Lx*2,3)
#提取边缘：
for _ in [0]:
    pic1=pic*0
    pic1[:,:,3]=pic[:,:,3]
    pic=edge(pic,pic1)
    pic=1-pic
pic2=(2*pic)**2/4
pic2=np.minimum(pic2,1)
pic=np.vstack((pic,pic2))
pic=np.hstack((pic,pic[:,:400]*1))
for _ in [0]:
    #pic=flip90_left(pic)
    pic=np.minimum(pic,0.99)
    pic=np.maximum(0.01,pic)
    pic[:,:,-1]=0.99
    plt.imshow(pic)
    #plt.axis('off') #不显示坐标轴
    plt.show()
