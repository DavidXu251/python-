
import numpy as np
from numpy.fft import fft2,ifft2,fftshift,ifftshift
from PIL import Image

data=np.array(Image.open('实验图片.png')
              .convert('L'))

data2=fft2(data)
print(data2.shape)

size=500
data2[:size]=0.5
#data2[-size:]=0
#data2[:, :size]=0
#data2[:, -size:]=0

data3=ifft2(data2)



(
Image.fromarray(
    data.real.astype('uint8'))
    .convert('L').save('黑白原始图片.png')
)

(
Image.fromarray(
    data3.real.astype('uint8'))
    .convert('L').save('结果.png')
)

data2=np.log(np.abs(data2))
data2=data2/np.max(data2)*128
(
Image.fromarray(
    data2.astype('uint8'))
    .convert('L').save('傅里叶.png')
)
print(data.shape)
print(data2.shape)
print(data3.shape)
from os import system
system('结果.png')
system('黑白原始图片.png')
system('傅里叶.png')




