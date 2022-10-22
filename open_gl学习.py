

import pygame
import time
from OpenGL.GL import *
from OpenGL.GLU import *

#---初始化pygame和定义窗口大小---
pygame.init()
#OPENGL|DOUBLEBUF=DOUBLEBUF|OPENGL
#DOUBLEBUF:双缓冲模式（推荐和 HWSURFACE 或 OPENGL 一起使用）
#创建一个 OPENGL 渲染的显示
screen=pygame.display.set_mode((640,480),
                        pygame.OPENGL|pygame.DOUBLEBUF)


#---元组定义---
#定义正方体的xyz坐标点
CUBE_POINTS = (
    (0.5, -0.5, -0.5),
    (0.5, 0.5, -0.5),
    (-0.5, 0.5, -0.5),
    (-0.5, -0.5, -0.5),
    (0.5, -0.5, 0.5),
    (0.5, 0.5, 0.5),
    (-0.5, -0.5, 0.5),
    (-0.5, 0.5, 0.5)
    )

#定义RGB颜色

CUBE_COLORS = (
    (1, 0, 0),
    (1, 1, 0),
    (0, 1, 0),
    (0, 0, 0),
    (1, 0, 1),
    (1, 1, 1),
    (0, 0, 1),
    (0, 1, 1))

# 定义面，四个点构成一个面

CUBE_QUAD_VERTS = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
    )

# 定义线，两个点构成一个线

CUBE_EDGES = (
    (0,1),(0,3),
    (0,4),(2,1),
    (2,3),(2,7),
    (6,3),(6,4),
    (6,7), (5,1),
    (5,4), (5,7),
    )


#---定义画立方体函数---

def drawcube():

    # "绘制正方体"，zip和list法

    allpoints = list(zip(CUBE_POINTS, CUBE_COLORS))

     

    #画面积---开始---结束---
    glBegin(GL_QUADS)
    for face in CUBE_QUAD_VERTS:
        for vert in face:
            pos, color = allpoints[vert]
            #在第2个for下面
            glColor3fv(color)
            glVertex3fv(pos)
    #与第1个for对齐
    glEnd()
    #边线颜色黑色
    glColor3f(0, 0, 0)
    # 绘制线---开始---结束---
    glBegin(GL_LINES)
    for line in CUBE_EDGES:
        for vert in line:
            pos, color = allpoints[vert]
            glVertex3fv(pos)
    glEnd()


#---主函数---
def main():
    glEnable(GL_DEPTH_TEST)
    #初始化 摄像头
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0,640/480.0,0.1,100.0)
    glTranslatef(0.0, 0.0, -3.0)
    glRotatef(25, 1, 0, 0)
    #启动循环---

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        #清除屏幕
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        

        #摄像机旋转
        glRotatef(0.1,0,0.1,0)
        drawcube()
        #刷新画面
        pygame.draw.rect(screen,
                    pygame.Color(150,150,150),
                    pygame.Rect(0,0,100,100),
                    0
                    )
        time.sleep(1/60)
        pygame.display.flip()



  

if __name__ == '__main__':
    main()
