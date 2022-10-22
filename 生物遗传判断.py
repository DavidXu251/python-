
#画出遗传图谱
#怎么表示遗传图谱：
#一个人用几个符号表示 如-m +f
#多个人之间用空格隔开  不同代之间用换行隔开
#同代之间、不同家庭，用/隔开

#具体怎么表示一个人：
#- 表示正常
#+ 表示患病
#? 表示未知
#---表示不携带致病基因

#m表示男性
#f表示女性
#性别这部分不写也行


class Person:
    def __init__(self,info,g_count,f_count):
        self.parents=[]
        self.kids=[]
        self.g_count=g_count
        self.f_count=f_count
        self.info=info
        
        if '-' in info:
            self.sick='-'
        elif '+' in info:
            self.sick='+'
            
        if 'm' in info:
            self.gender='m'
        elif 'f' in info:
            self.gender='f'
        else:
            self.gender=None
    def add_parent(self,parent):
        pass
    def add_child(self,child):
        pass
    def __str__(self):
        return self.info+str(self.g_count)+str(self.f_count)
        pass
    def __repr__(self):
        return self.__str__()
image='''
-m -f
+m
'''.strip('\n')

i_lst=[]
for generation in image.split('\n'):
    g_count=-1
    g_count+=1
    g_lst=[]
    i_lst.append(g_lst)
    for family in generation.split('/'):
        f_count=-1
        f_count+=1
        f_lst=[]
        g_lst.append(f_lst)
        for person_info in family.strip(' ').split(' '):
            person=Person(person_info,
                       g_count,f_count)
            f_lst.append(person)
            
            
print('获取了家谱图：',i_lst)











