


#使用矩阵的概念来解方程


#如果不用库，自己做：

def show():
    global data
    for line in data:
        print(line)
    print()

var_count=3
data=[[1,1,1,1],
           [1,2,1,1],
           [3,5,4,1]]

for i in range(3):
    scale=data[i][i]
    for j in range(0,4):
        data[i][j]/=scale
    
    
    for a in range(i+1,3):
        scale2=data[a][i]
        for b in range(0,4):
            data[a][b]-=data[i][b]*scale2
    show()

for i in range(2,-1,-1):
    value=data[i][i+1]
    for j in range(0,i):
        data[j][-1]-=value*data[j][i]
        data[j][i]=0
    show()



#也可以用库：
#pip config set global.index-url
#    'https://pypi.tuna.tsinghua.edu.cn/simple'
import numpy as np
a=np.matrix([[1,1,1],[1,2,1],[3,5,4]])
b=np.matrix([[1],[1],[1]])

print(np.linalg.solve(a,b))


