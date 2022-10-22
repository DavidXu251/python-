
#百度的句法分析接口
from aip import AipNlp
#在百度管理中心 点击创建应用
#获取app_id api_key secret_key
client=AipNlp('21626284',
    '4jwGPCynrTGaCyf8CavFSvYj',
    '57Vz5eoHcbpRwm2WrnHzaIH3GPBgH68m',
    )
def analyze(text):
    items=client.depParser(text)['items']
    words=[x['word'] for x in items]
    ptrs=[]
    for x in items:
        if x['head']==0:
            ptrs.append('no')
        else:
            ptrs.append(words[x['head']-1])
    return words,ptrs
def pprint(lst):
    for i in lst:
        print(i,end=' ')
    print()
book=open('小蘑菇.txt','rb').read().decode('gbk')

for sentence in book.split('，'):
    words,ptrs=analyze(sentence)
    pprint(words)
    pprint(ptrs)
    input()
