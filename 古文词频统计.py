

import re

from collections import Counter
counter=Counter()

import codecs
'''
counter.update(codecs.open('新唐书.txt',
    encoding='ANSI').read())

counter.update(codecs.open('明史.txt',
    encoding='utf-8').read())
'''        
counter.update(codecs.open('古文观止.txt',
    encoding='utf-8').read())

for i in '''[]（）《》“”。，、！？：；
\n\r\u3000\u0020\u00A0○
一二三四五六七八九十 1234567890 东南西北

''':
    del counter[i]




from collections import defaultdict
dictionary=defaultdict(list)
dict_lines=codecs.open('古汉语字典 完整.txt',
        encoding='utf-8'
        ).read().split('\n\n')
dict_lines=[x for x in dict_lines
            if x!='' and ord(x[0])>256]

for i in range(0,len(dict_lines)-1):
    line=dict_lines[i]
    line2=dict_lines[i+1]
    if len(line)<=10 and '。' not in line:
        word=line[0]
        dictionary[word].append(
            line+'\n'+line2)




import sys
file=codecs.open(
    '古汉语字典 词频2.txt','w',
    encoding='utf-8')
origin_stdout=sys.stdout
sys.stdout=file


    

for i,(word,freq) in enumerate(
        counter.most_common(2000)):
    print(i,freq,word)
    for line in dictionary[word]:
        x=line
        x=re.sub(r'（.+?）','',x)
        x=re.sub(r'“.+?”',
                lambda s: '。' if '。' in s.group() else s.group(),
                x)
        x=re.sub(r'[❷❸❹❺❻❼❽❾❿⓫⓬⓭⓮⓯⓰⓱⓲⓳⓴]',
            lambda s: '\n'+s.group(), x)
        x=x.replace('：','')
        x=x.replace(' ','')
        x='。'.join([i for i in x.split('。')
            if '《' not in i
        ])
        print(x)
    print()

file.close()

sys.stdout=origin_stdout

import os
os.system('notepad 古汉语字典 词频2.txt')

'''

for i,(word,freq) in enumerate(
        counter.most_common(10)):
    print(dictionary[word])
'''



    
