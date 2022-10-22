
data=( open('牛津英汉词典.txt',  'rb')
        .read().decode('utf-8') )
dic={}
for line in data.split('\n'):
    line=line.split()
    if len(line)==2:
        dic[line[0]]=line[1]

note=open('我的生词.txt',  'w')

import pygame
pygame.init()
width,height=600,500
screen=pygame.display.set_mode(
    (width,height))
screen.fill((255,255,255))
pygame.display.flip()

pygame.font.init()
font=pygame.font.Font(
    '微软雅黑.ttf',
    30)
#SysFont(字体名,按照像素大小,是否粗体,斜体)
pic=font.render('hello',True,(0,0,0))
screen.blit(pic,(0,0))

pygame.display.flip()






