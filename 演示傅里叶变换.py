size = width, height = 600, 500
printtime = 0
white = 255, 255, 255
black = 0, 0, 0
screenX, screenY = 0, 0
actors = []
text_size = 50

def nothing(*args): pass


SquareAve=lambda a,b:((a**2+b**2)*0.5)**0.5


for _ in [0]:
    import pygame
    pygame.init()
    screen = pygame.display.set_mode(size)
    findevent = pygame.event.get
    import time
    game_start_time=time.time()
    import random
    pygame.font.init()
    worder=pygame.font.SysFont('',text_size)
def newlife(flips=1):
    global actors, screen
    pygame.display.flip()
    screen.fill((0, 0, 0))
    global mouse, printtime
    for eve in findevent():
        if eve.type == 1:  # 鼠标进入这个窗口
            pass
        elif eve.type == 4:  # 鼠标移动
            mouse = eve
        elif eve.type == 12:  # 退出键
            print('显示了', printtime, '次')
            all_time= time.time() - game_start_time
            average_fps=printtime/all_time
            print('显示了',all_time,'秒')
            print('平均帧数:',average_fps,'张/秒')
            pygame.quit()
            import sys
            sys.exit()
        else:
            pass
    printtime += 1
##    for x in actors:
##        screen+x+x+x+x+x+x+x+x+x+x+x+x
    for _ in range(2):
        for x in actors:
            screen+x
newlife()


##        pygame.draw.rect(scr, self.color,
##                         (self.Sx - screenX, self.Sy - screenY
##                          , self.Lx, self.Ly), 0)


        

import numpy as np
import random
color_asked=(255,255,255)
width_asked=1
Sx_start=100
Sy_start=screen.get_size()[1]/2
Num_lines=25
def refresh():
    global S_lines,R_lines,ou_lines,wave,wave2
    S_lines,R_lines,ou_lines=[],[],[]
    for _ in range(Num_lines):
        S_lines.append(random.randint(2,10))
        R_lines.append(random.randint(5,10))
        ou_lines.append(random.randint(-10,10))
    S_lines=np.array(S_lines)*1.0
    R_lines=0*S_lines
    ou_lines=np.array(ou_lines)*2*np.pi/720
    wave=[int(Sy_start)]
    wave2=[(Sx_start,Sy_start)]
refresh()
while True:
    Sx_here,Sy_here=Sx_start,Sy_start
    R_lines+=ou_lines
    for S,R in zip(S_lines,R_lines):
        Sx_move=np.sin(R)*S
        Sy_move=np.cos(R)*S
        pygame.draw.line(screen,
                color_asked,
                (Sx_here,Sy_here),
                (Sx_here+Sx_move,Sy_here+Sy_move),
                 width_asked)
        Sx_here+=Sx_move
        Sy_here+=Sy_move
    wave[0:0]=[int(Sy_here)]
    wave2[0:0]=[(int(Sx_here),int(Sy_here))]
    del Sx_move,Sy_move
    
    for x,y in zip(range(200,width),wave):
        pass
        screen.set_at((x,y),color_asked)

    pygame.draw.lines(screen,color_asked,False,
                      list(zip(range(200,width),wave)),
                      width_asked)
    pygame.draw.lines(screen,color_asked,False
                      ,wave2,width_asked)
    if len(wave)>width:
        wave.pop()
        wave2.pop()
    if printtime%1000==0:
        refresh()
        pass
    newlife()
      
