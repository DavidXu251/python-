








file=open('./我的模型/hello.obj', 'w')
file.write('''
v 0,0,0
v 0,1,0
v 1,0,0

f 0/1/2
''')
file.close()

import os
os.system('cd ./我的模型 && hello.obj')





