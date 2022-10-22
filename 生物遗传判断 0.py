
class Mynone:
    def __and__(self,right):
        return False
    def __or__(self,right):
        return False
    def __eq__(self,right):
        return False
    def __str__(self):
        return 'none'
    def __repr__(self):
        return 'none'
none=Mynone

class Obj:
    def __init__(self,name='none'):
        self.name=name
        self.dict=dict()
    def __str__(self):
        return self.name
    def __repr__(self):
        return str(self)

class Relation(Obj):
    def __getitem__(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return none
    def __setitem__(self,key,val):
        def do():
            self.dict[key]=val
            print(f'{self.name}[{key}]={val}')
            global to_check
            to_check.append(val)
        if key is none:
            return
        if key not in self.dict:
            do()
        elif self.dict[key]!=val:
            do()        


parent,child,male,sick=[
    Relation(s)
    for s in '''dad,mom,child,male,sick'''.replace('\n','').split(',')
    ]

to_check=a,b,c,d=[
    Obj(s)
    for s in 'a,b,c,d'.split(',')
    ]
parent[a]=b
parent[a]=c
male[a]=True
male[b]=True
male[c]=False
sick[a]=True
sick[b]=sick[c]=False

explicit=none
with_X=none

for self in to_check:
    print(f'in {self}:')
    if ( (not sick[dad[self]])
        and (not sick[mom[self]])
        and sick[self] ):
        explicit=True
        print('is explicit')
    
        







