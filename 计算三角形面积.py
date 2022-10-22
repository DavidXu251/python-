'''输入3边长，如果可以构成三角形，就输出
面积和边长和文字，否则就提示不能构成三角形'''
a=input('请输入三角形的三边，用空格隔开。')
a=a.replace(',' , ' ')
a=a.split()
a=[float(x) for x in a]
a.sort()
[a,b,c]=a
print('三边长是',a,b,c)
if a+b<=c:
    print(f'{a}+{b}<={c} 不能构成三角形')
else:
    print(f'{a}+{b}>{c} 可以构成三角形')
    C=a+b+c
    p=C/2
    S=(p*(p-a)*(p-b)*(p-c))**0.5
    print('周长是:',C)
    print('面积是:',S)



