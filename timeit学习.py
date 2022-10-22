
import numpy as np
import time
import timeit

def task():
    time.sleep(1)
    
number=10
print(timeit.timeit(task,
                    number=number)/number)


