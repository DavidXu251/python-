


import os
def deep_search(path,key):
    for p in os.listdir(path):
        if key.lower() in p.lower():
            print(path+'\\'+p)
        try:#如果是文件夹就往下搜索
            deep_search(path+'\\'+p,key)
        except NotADirectoryError:
            pass
    return None


deep_search(r'''
C:\Users\XUDEMING\OneDrive\桌面\edge的文件夹\mingw64\mingw64
'''.replace('\n',''),
            key='msys')
