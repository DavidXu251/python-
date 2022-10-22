#尝试计算表达式
def split(a):
    b=['']
    for x in a:
        if x in '+-*/':
            b.append(x)
            b.append('')
        elif x==' ':
            pass
        else:
            b[-1]+=x
    return b
a='234*32/15+32/2'
a=split(a)
level={'+':1,   '-':1,
       '*':2,   '/':2  ,
       'start':0}
a.insert(0,'start')
key=1
print(a)
while True:
    sym1,sym2=a[key-1],a[key+1]
    if level[sym1]>=level[sym2]:
        key-=2
    elif level[sym1]<level[sym2]:
        key+=0
    a[key:key+3]=[eval(''.join(
        str(x) for x in a[key:key+3]     )   )]
    print(a)
    if len(a)==2:
        break
