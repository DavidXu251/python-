from time import *
def test(fun):
    def newfun(*tup):
        print('开始测试函数')
        start=time()
        ret=fun(*tup)
        end=time()
        print('函数结束，用时',end-start,'秒',ret)
        return ret
    return newfun
def funA():
    a=0
    for _ in range(1000_000):
        a+=1
funA=test(funA)
funA()
def funB():
    a=0
    code=compile('a+=1','','exec')
    for _ in range(1000_000):
        exec(code)
funB=test(funB)
funB()


    
