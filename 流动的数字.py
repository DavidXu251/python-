
def make_move(a):
    b=[0]*(len(a)+2)
    for place,delta in enumerate(a):
        b[place]+=delta/3
        b[place+1]+=delta/3
        b[place+2]+=delta/3

    return b


if __name__ == "__main__":
    a=[0,81,0]
    b=[0,0,0,0,0]
    while True:
        a=make_move(a)
        if len(a)>10:
            a=a[1:-1]
        for i in a:
            print(str(i)[:2],end = ' ')
        print()
        # print('a=',a)