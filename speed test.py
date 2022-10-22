import time
test=10**7

t=time.time()
s=0
for i in range(test):
    s+=i
print(time.time()-t,'秒')
print(test/(time.time()-t) /10**6, '百万行/秒')
print(s)

