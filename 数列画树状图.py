


#已知数列a[n]: 1,_,_,2,_,_,_,3,_,_,_,_,_,_...
#满足a[n] in {a[n+1], a[n+2], a[n+3]}
#求a[20]

import pyecharts
import xmind

w=xmind.load('test.xmind')
s1=w.getPrimarySheet()
s1.setTitle('first sheet')

r1=s1.getRootTopic()
r1.setTitle('根')
r2=r1.addSubTopic()
r2.setTitle('zhiye')



