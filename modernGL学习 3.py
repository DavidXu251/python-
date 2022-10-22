

import os

import pygame
pygame.init()
screen=pygame.display.set_mode(
    (600,600),
    pygame.OPENGL | pygame.DOUBLEBUF
)

import moderngl_window as mglw
class Example(mglw.WindowConfig):
    gl_version = (3, 3)
    title = "ModernGL Example"
    window_size = (1280, 720)
    aspect_ratio = 16 / 9
    resizable = True
    resource_dir = '可莉模型'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @classmethod
    def run(cls):
        mglw.run_window_config(cls)

Example.run()
