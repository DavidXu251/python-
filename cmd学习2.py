import os
import sys
import subprocess as sp


cmd=sp.Popen(
    #'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.8\Python 3.8 (64-bit)',
             shell=True,
             stdin=-1,
             stdout=-1,
             )
cmd.stdin.write(b'\n')
while True:
    print(cmd.stdout.read().decode('gbk'),end='')
    #cmd.stdin.write(sys.stdin.read())
