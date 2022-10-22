class Count:
    def __init__(self,sth):
        self.dic={i:1 for i in sth}
    def update(self,sth):
        for i in sth:
            try:
                self.dic[i]+=1
            except KeyError:
                self.dic[i]=1
    def __str__(self):
        return str(self.dic)
    __repr__=__str__

pockets={}#{'word':{'w','w','w'} }
file=open("小蘑菇2.txt",'rb')
line=None
size=2
while line!='':
    line=file.readline().decode('utf-8')
    for i in range(len(line)-size):
        try:
            pockets[line[i]].update(line[i+1:i+size])
        except KeyError:
            pockets[line[i]]=Count(line[i+1:i+size])
print(pockets["蜜"])
