
import time
t1=time.time()
mb=b'a'*1024*1024

file=open('F:/hello.txt', 'wb')
for i in range(10):
    file.write(mb)

t2=time.time()
file.close()
print(t2-t1)
