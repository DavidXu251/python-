
import time
import random
import matplotlib.pyplot as plt

def check_func_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time


# Optimized bubble sort function
def bubble_sort(my_list):
    N = len(my_list)
    for i in range(1,N):
        swapped = False
        for j in range(0,N-i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                swapped = True
        if swapped == False:
            break
    return my_list


# Merge sort definition
def merge_sort(m):

    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


# Merge function definition
def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison
        # to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])

    return result


bubble_times=[]
merge_times=[]

for size in range(0,5000,20):
    print(size)
    ls=[random.randint(0,size) for _ in range(size)]
    bubble_times.append(
        check_func_time(bubble_sort,ls))
    
    ls=[random.randint(0,size)
        for _ in range(size*10)]
    merge_times.append(
        check_func_time(merge_sort,ls))
    plt.cla()
    plt.plot(bubble_times)
    plt.plot(merge_times)
    plt.pause(0.000001)
