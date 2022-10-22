
from collections import Counter
help(Counter)
book=open('小蘑菇.txt','r').read()
class topic:
    sub={}
    group=Counter()
    def learn(self,new,old):
        self.group[new]+=1
        


root=topic()
for ptr,new_word in enumerate(book,start=101):
    recent=book[ptr-100:ptr]
    old_word=book[ptr-101]
    
    root.learn(new_word,old_word)

    
