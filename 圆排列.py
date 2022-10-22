
#导入笛卡尔积
from itertools import product
used=set()
ls=[]

for case in product('rgb', repeat=12):
    if case not in used:
        used.update(case[i::step]+case[:i:step]
                    for i in range(len(case))
                    for step in (1,-1)
                    )
        ls.append(''.join(case))

print(len(ls))
print(len(used))
#print('\n'.join(ls))
