def tutu(my_id):
    while True:
        yield True

def crab(my_id):
    while True:
        yield False

def repeater(my_id):
    global record
    yield True#第一次先合作
    while True:
        yield record[not my_id][-1]
def noter(my_id):
    note=0
    yield True#第一次先合作
    while True:
        if record[not my_id][-1]==False:
            note+=1
        note=note*0.5
        if note>=0.6:
            print('我记仇了')
            yield False
        else:
            yield True
players=[tutu,crab,repeater,noter]
coins=[0]*len(players)
def human(my_id):
    print('你是'+str(my_id+1)+'号')
    while True:
        yield int(input('判断：'))

def play(p1_func, p2_func, quiet=False):
    global record
    record=[ [],[] ]
    p1=p1_func(my_id=0)
    p2=p2_func(my_id=1)
    p1_coin=0
    p2_coin=0

    for i in range(20):
        p1_res,p2_res=next(p1),next(p2)
        record[0].append(p1_res)
        record[1].append(p2_res)

        if p1_res:
            p1_coin-=1
            p2_coin+=3
        if p2_res:
            p2_coin-=1
            p1_coin+=3
        if not quiet:
            print('是' if p1_res else '否',
                     '是' if p2_res else '否', end=' ')
            print(p1_coin,p2_coin)
    return p1_coin,p2_coin

##play(
##        human,
##        noter,
##       )
for i in range(len(players)-1):
    for j in range(i+1,len(players)):
        c1,c2=play(players[i],players[j], quiet=True)
        coins[i]+=c1
        coins[j]+=c2
        print(i,j)
print(coins)
