from urllib import request
print('import succeed')
url=r'''https://editor.p5js.org/'''

name=r'connor.mp3'
place=''

print('getting response from: '+url)
url=request.Request(url)
response=request.urlopen(url)


print('response done. Now reading')
read=response.read()
print('responce read')
print(f'size(read) is {len(read)} bytes')
if type(read)==bytes:
    with open(place+name,'wb') as a:
        a.write(read)
    print('file saved')
