import subprocess as sp
import sys
cmd=sp.Popen('python',
        stdin=sp.PIPE,stdout=sp.PIPE,
        stderr=sp.STDOUT,
        shell=True,
             )
import time
time.sleep(1)
got=sp.check_output('cmd.exe python',shell=True)
print(got.decode('gbk'))
while True:
    print(' ',end='')
    got=cmd.stdout.read()
    if type(got)==bytes:
        got=got.decode('gbk')
    print(got,end='')






