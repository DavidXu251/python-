signs=[None,100,100,100]
allfloors=len(signs)-1
startfloor=2
aimfloor=5
print(signs,'from',startfloor,'to',aimfloor,\
'接下来画分类讨论树')
tree=[['st ',startfloor]]

def upleaf(leaf):
    global signs, allfloors
    record,floornow=leaf
    record+=' up'
    floornow+=signs[floornow]
    if floornow<=allfloors and floornow>0:
        return [[record,floornow]]
    else:
        return []


def downleaf(leaf):
    global signs, aimfloor
    record,floornow=leaf
    record+=' down'
    floornow-=signs[floornow]
    if floornow<=allfloors and floornow>0:
        return [[record,floornow]]
    else:
        return []



def newtree(tree):
    newtree=[]
    for leaf in tree:
        newtree+=downleaf(leaf)
        newtree+=upleaf(leaf)
    print(newtree)
    
    return newtree
tryingtimes=0
while tryingtimes>-1:
    tryingtimes+=1
    tree=newtree(tree)
    for leaf in tree:
        if leaf[1]==aimfloor:
            print('成功,方法如下 ',leaf,'次数:',tryingtimes)
            tryingtimes=-1
    if tree==[]:
        print('失败，无解')
        tryingtimes=-1
