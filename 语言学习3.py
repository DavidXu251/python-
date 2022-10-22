book=open("小蘑菇.txt",'r').read()
vocabulary={'字':{'符':3,'母':2,'号':4},
            }
for i in range(len(book)-1):
    left=book[i]
    right=book[i+1]
    try:
        vocabulary[left][right]+=1
    except KeyError:
        try:
            vocabulary[left][right]=1
        except KeyError:
            vocabulary[left]={}


string='>>'
while True:
    got=input(string)
    if got=='':
        string='>>'
    else:
        string+=got
    
    try:
        possible=vocabulary[string[-1]]
        possible=dict(sorted(
            possible.items(),
            key=lambda x : x[-1],
            reverse=True,
            ))
    except:
        possible={}
    for val,key in zip(
            possible.keys(),possible.values()):
        print(f'{string[-1]}{val}-{key}  ',end='')
    print()



                  
