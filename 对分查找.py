def pt(a):
    for i in a:
        print(str(i)[:4])

import random
a=[0]
for i in range(7):
    a.append(a[-1]+random.random())
for i in range(len(a)):
    a[i]=int( (a[i]*10)//1 )
print(a)

start=0
end=len(a)-1
mid=(start+end)//2
print(f'{start=} {end=} {mid=} {a[mid]}')

key=float(input('key='))

while True:
    if key<a[mid]:
        end=mid-1
    elif a[mid]<key:
        start=mid+1
    
    mid=(start+end)//2
    print(f'{start=} {end=} {mid=} {a[mid]}')

    if start>end:
        print(-1)
        break
    if a[mid]==key:
        print(mid)
        break





