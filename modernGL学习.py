

import numpy as np
import time

import pygame
pygame.init()
screen=pygame.display.set_mode(
    (600,600),
    pygame.OPENGL | pygame.DOUBLEBUF
    )




import moderngl
ctx=moderngl.create_context()

prog = ctx.program(
    vertex_shader='''
    #version 330
    in vec2 vert;
    in vec4 vert_color;
    out vec4 frag_color;
    uniform vec2 scale;
    uniform float rotation;
    void main() {
        frag_color = vert_color;
        float r = rotation * (0.5 + gl_InstanceID * 0.05);
        mat2 rot = mat2(cos(r), sin(r), -sin(r), cos(r));
        gl_Position = vec4((rot * vert) * scale, 0.0, 1.0);
    }
    ''',
    fragment_shader='''
    #version 330
    in vec4 frag_color;
    out vec4 color;
    void main() {
        color = vec4(frag_color);
    }
    ''',
)

scale = prog['scale']
rotation = prog['rotation']

scale.value = (0.5, 0.5)

vertices = np.array([
    1.0, 0.0,
    1,   0.4,  1, 0.5,

    -0.5, 0.86,
    0.0, 0.6, 1.0, 0.5,

    -0.5, -0.86,
    1.0, 0.3, 0.5, 0.5,
], dtype='float32')

vbo = ctx.buffer(vertices)
vao = ctx.simple_vertex_array(prog, vbo, 'vert', 'vert_color')


count=0
while True:
    count+=1
    time.sleep(1/120)
    pygame.display.flip()
    pygame.event.get()
    
    ctx.clear(1.0, 1.0, 1.0)
    ctx.enable(moderngl.BLEND)
    
    rotation.value = count/120
    vao.render(instances=3)




