from copy import deepcopy
from numpy import array,ndarray
arr1=[5,6,7,6,5,4,3]
arr2=[1,2,3]
def prtt(arr,behind=0,Len=2,end=30):
    string=''#去除小数点并右对齐
    #每个元素有Len个空格的空间向右对齐
    #+++++_1/_2/_____3/_2/ xxxxxx
    #^front^         ^Len^     ^behind^ ^end
    for x in arr:
        string+=str(x).rjust(Len,'_')
    string+=behind*'x'
    ans=string.rjust(end,'+')
    print(ans);return ans
prtt(arr1)
prtt(arr1,spc=2)
def sus(arr1,arr2,pos):
    prtt(arr1)
    
    n=zip(arr1[pos-1:],arr2)
    return [x-y for (x,y) in n]
def div(arr1,arr2):
    pass
