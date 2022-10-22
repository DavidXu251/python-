

def func_to_compile():
    a=[1,2]
    a.sort()

import dis
dis.dis(func_to_compile)
