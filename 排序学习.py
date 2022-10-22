
def merge_sort(lst):
    if len(lst)<=1:
        print('bottom',lst)
        return lst 
    left=lst[:len(lst)//2]
    right=lst[len(lst)//2:]
    print('split:', lst,'->',left,right)
    
    left=merge_sort(left)
    print('half done:', lst)
    right=merge_sort(right)
    
    #merge now:
    merged=[]
    left_saved=left[:]
    right_saved=right[:]
    while left and right:
        if left[0]<=right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left+right)
    print('merge:', merged, '<-',
          left_saved,right_saved)
    return merged

import random
ls=list(range(8))
random.shuffle(ls)
print(merge_sort(ls))
    
