
#已知f(x)定义域是正整数N*，值域包含于N*
#又，任意正整数x，f(f(x))=3x
#求f(2022)-f(2019)

checked={}
to_check={1:2}

while len(to_check)!=0:
    x,fx=to_check.popitem()
    if x<=200:
        to_check[fx]=3*x
        for y,fy in checked.copy().items():
            if x-y==fx-fy:
                for i in range(y+1,x):
                    fi=fx-x+i
                    checked[i]=fi
                    to_check[fi]=3*i
                    #print(i,x,y,fx,fy)
    checked[x]=fx

import matplotlib.pyplot as plt
data=checked.items()
plt.scatter([x[0] for x in data], [x[1] for x in data])
plt.plot([0,2000],[0,4000])
plt.show()






        
    
