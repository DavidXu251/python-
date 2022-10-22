signs=[None,3,5,2,1,0,2]
startfloor=3
aimfloor=2
height=len(signs)-1
def clear(signs):
    me=1
    end=len(signs)-1
    while me<=end:
        signs[me]=0
        me+=1
    return signs

tree=clear(signs)
time=1
def down(floor):
    global signs
    aim=floor-signs[floor]
    if aim>0:
        return aim
    else:
        return 0

def up(floor):
    global signs
    aim=floor+signs[floor]
    if aim<=height:
        return aim
    else:
        return 0

def grow(tree,floor):
    global time,signs
    floor=1
    nexttime=time+1
    for leaf in tree:
        if leaf==time:
            
        
    





