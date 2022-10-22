def shift1(out,movement=1):
    out=[chr(ord(x)+movement) for x in out]
    outt=''
    for x in out:outt+=x
    return outt
def shift2(out,movement=1):
    outt=''
    for x in out:
        outt+=chr(ord(x)+movement)
    return outt
from time import *
def test(fun,a,b):
    print('开始测试函数')
    start=time()
    ret=fun(a,b)
    end=time()
    print('函数结束，用时',end-start,'秒',ret)
strr=input('put in strings:')
move=0
while move<30:
    move+=1
    print(shift1(strr,move))

