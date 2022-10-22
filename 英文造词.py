
file=open('英汉词典.txt', encoding='utf-8')

count=0
for line in file.read().split('\n'):
    if line!='':
        word=line.split(' ')[0]
        if (set(word).issubset(set('soldier'))
            and len(set(word))==len(word)):
            print(line)
            count+=1

print('一共搜索到了', count, '个')
