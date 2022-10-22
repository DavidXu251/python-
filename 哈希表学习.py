
class hashmap:
    def __init__(self, dic, size=10):
        self.size=10
        self.buckets=[[] for i in range(size)]
        
        for key,val in dic.items():
            self.add( key,val )
            
    def add(self,key,val):
        hsh=hash(key)%self.size
        bucket=self.buckets[hsh]
        bucket.append( (key,val) )
    def get(self,key):
        hsh=hash(key)%self.size
        bucket=self.buckets[hsh]
        for key2,val in bucket:
            if key2==key:
                return val
        raise ValueError

from random import randint
from pprint import pprint
m=hashmap(
    {randint(0,100) : randint(0,100)
     for i in range(100)
     })

m.add('a',30)
print(m.get('a'))

pprint(m.buckets)

