
class Word:
    def __init__(self,name='东西'):
        self.name=name
        self.voc={} # {'小明': Word('小明')}
        self.porp=[]
    def add_voc(self):
        pass
        
    def get_word(self, name):
        if name in self.voc:
            return self.voc[name]
        else:
            obj=Word(name)
            self.voc[name]=obj
            return obj
    def _str__(self):
        return self.name
    def __repr__(self):
        return self.name

class Relation:
    def __init__(self,):
        pass
    #X.爸爸.爸爸==X.爷爷
    #Y==X.爸爸  =>  X=Y.儿子
    
    
universe=Word(name='')

sent='小明的爸爸是小徐'
'小徐的爸爸是小华'
'小明的爷爷是谁'


        

import jieba
def read_sent(sent):
    words=list(jieba.cut(sent))
    print(words)
    obj_now=universe.get_word(words[0])
    i=1
    while i<len(words):
        word=words[i]
        if word=='的' and i!=0 and i!=len(words):
            obj_now=obj_now.get_word(words[i+1])
            print('->',words[i+1])
            i+=2
            
        elif word=='是':
            obj_now.name=words[i+1]
            i+=2
        else:
            i+=1
            print('strange:', word)
    return obj_now

print('=', read_sent('小明喜欢的颜色是红色'))
print('=', read_sent('小明的爸爸的奶奶'))









