
import pyrr
look_at=pyrr.Matrix44.look_at

import numpy as np
from numpy import sin,cos,pi,sqrt

import time

import ctypes
win32=ctypes.windll.user32
win32.SetProcessDPIAware()

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
    in vec3 vert;
    in vec2 tex;
    
    out vec2 frag_tex;
    
    void main() {
        gl_Position=vec4(vert,1);
        gl_Position*=0.1;
        gl_Position.y-=0.5;
        
        gl_Position.w=1;
        frag_tex=tex;
    }
    ''',
    
    fragment_shader='''
    #version 330
    in vec2 frag_tex;
    uniform sampler2D face;
    
    out vec4 color;
    
    void main() {
        color = texture(face, frag_tex);
    }
    ''',
)
print(prog._members)


from moderngl.ext.obj import Obj
model=Obj.frombytes(
    open('./可莉模型/可莉.obj', 'rb').read())
vbo = ctx.buffer(model.pack(
    'vx vy vz'
))
tbo = ctx.buffer(model.pack(
    'tx ty'
))


from PIL import Image
img = Image.open('./可莉模型/衣服.jpg')
face=ctx.texture(img.size, 3, img.tobytes())
prog['face']=0
face.use(0)


vao = ctx.vertex_array(
    prog,
    [
        (vbo, '3f', 'vert'),
        (tbo, '2f', 'tex'),
    ]
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
    ctx.enable(moderngl.BLEND)
    
    vao.render()




