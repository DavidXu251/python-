
chords_str=(
'''
#喜羊羊
1 1 1 5
6 4 5 1
4 4 1 1
2 1 5 5
1

#日常ed
1 5 1 5
1 5 4 1
1 5 1 5
1 5 3 6 1 4 1
1 6 3 2 4 4 1 5

#faded
6 4 1 5
6 4 1 5
6 6 4 3
6 6 4 3 6
2 5


'''
)
chords=[]
for i in chords_str.split():
    try:
        chords.append(int(i))
    except ValueError:
        if i.startswith('#'):
            pass
        else:
            raise ValueError('Unknown word'+i)
        
import numpy as np
table=np.zeros((8,8), dtype=int)
for left, right in zip(chords[:-1],chords[1:]):
    table[left, right]+=1
##for i in range(table.shape[0]):
##    table[i, i]=0

print(table)
import matplotlib.pyplot as plt
print(dir(plt))
plt.imshow(table)
plt.show()

