import time
a=0
i=0
'''
while True:
    i+=1
    print("haha",end="")
    for _ in range(i):
        print("a",end="")
    print()
    for _ in range(1000000):
        pass
'''

while True:
    a+=1
    print(a,end='')
    time.sleep(1)
    print(len(str(a))*"\b",end='')