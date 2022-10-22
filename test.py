

def f(x):
    return x<100

ls=[-3,10,51,1304, 10]

print(list( filter(f, ls)) )


'''
lst=[(1,2), (3,1), (5,3), (-4,3)]

def f(x):
    return x[1]

print(sorted(lst,
            key=f(lst),
            reverse=True))
'''
