
'''
make a encode and decode program that turns
a string into the code:

'123456'

1     5       9
  2 4  6   8
    3     7

'152463'
'''

def encode(data, rows=3):
    ls=[]
    period=(rows-1)*2
    for y in range(rows):
        x1=y
        x2=period-y
        while True:
            if x1>=len(data): break
            ls.append(data[x1])
            if x2>=len(data): break
            if y!=0 and y!=rows-1:
                ls.append(data[x2])
            x1+=period
            x2+=period
        
    return ''.join(ls)

def decode(code, rows=3):
    data=[None]*len(code)
    ls=list(code)
    period=(rows-1)*2
    for y in range(rows):
        x1=y
        x2=period-y
        while True:
            if x1>=len(data): break
            #ls.append(data[x1])
            data[x1]=ls.pop(0)
            if x2>=len(data): break
            if y!=0 and y!=rows-1:
                #ls.append(data[x2])
                data[x2]=ls.pop(0)
            x1+=period
            x2+=period
    return ''.join(data)

x='hello there'
print(x)
print(encode(x))
print(decode(encode(x)))







