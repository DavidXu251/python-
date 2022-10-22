
data=open('牛津英汉词典.txt', 'rb')\
      .read().decode('utf-8').split('\n')
data=[set(i) for i in data]
letter=input('要搜索的首字母:')

while True:
    target=set(input('中文:'))
    for line in data:
        if (letter[0]==letter
            and target in line):
            print(line)
