

import numpy as np
from numpy import sin,cos,pi,sqrt

import time

import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import pygame
pygame.init()
screen=pygame.display.set_mode(
    (1200,1200),
    pygame.OPENGL | pygame.DOUBLEBUF
    )




import moderngl
ctx=moderngl.create_context()

prog = ctx.program(
    vertex_shader='''
    #version 330

    in vec2 pos_v;
    out vec2 pos;
    
    void main(){
        gl_Position=vec4(pos_v, 0.0, 1.0);
        pos=pos_v;
    }
    ''',
    fragment_shader='''
    #version 330
    
    in vec2 pos;
    uniform float count;
    out vec4 color;

    vec2 pos1;
    vec2 pos2;
    float black1;
    float black2;
    float black;
    
    void main() {
        pos1=pos;
        pos1.x+=0.35;
        black1=sqrt(pos1.x*pos1.x + pos1.y*pos1.y);
        black1=
            sin(black1*12*3.1415 - count*0.02)*0.3+0.7;

        pos2=pos;
        pos2.x-=0.35;
        black2=sqrt(pos2.x*pos2.x + pos2.y*pos2.y);
        black2=
            sin(black2*12*3.1415 - count*0.02)*0.3+0.7;


        
        black=(black1+black2)/2;
        color=vec4(black,black,black,1);
        
        //color=(black1>0.999 || black2>0.999)
        //    ? vec4(1,0,0,1)*color : color;
        //color=(black1<0.401 || black2<0.401)
        //5    ? vec4(0,0.6,1,1)*color : color;
        
            
    }
    ''',
)

vbo=ctx.buffer(np.array([
    -1,-1,
    -1,1,
    1,-1,

    1,1,
    -1,1,
    1,-1,
],dtype='float32') )

vao = ctx.simple_vertex_array(
    prog,
    vbo,'pos_v',
    )



count=0
while True:
    count+=1
    time.sleep(1/120)
    pygame.display.flip()
    for eve in pygame.event.get():
        if eve.type==pygame.QUIT:
            pygame.quit()
            exit()
    
    ctx.clear(1.0, 1.0, 1.0)
    #ctx.enable(moderngl.BLEND)
    prog['count'].value=count
    vao.render()




