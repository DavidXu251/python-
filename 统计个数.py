
import matplotlib.pyplot as plt


s='''
5 3 3 6 4 4 4 5 4 4 7 6 6 6 6 6 6 5 6 6 4 6 5 3 3 3 4 6 4 4 3 3 5 6 6 6 3 3 7 4 5 4 5 6 5 4 6 6 4 3 5
'''

lst=[int(x) for x in s.split()]
count=[lst.count(x) for x in range(0,10)]

print(count)

plt.plot(count)
plt.show()
