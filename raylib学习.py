

import pyray as pr
pr.init_window(800,800,"hello")
pr.set_target_fps(60)

x=0

while not pr.window_should_close():
    x+=1
    
    pr.begin_drawing()
    pr.clear_background(pr.RAYWHITE)
    pr.draw_text(str(x),0,0, 60,pr.BLACK)
    pr.draw_text(
        "Congrats! You created your first window!",
        190, 200, 20, pr.LIGHTGRAY)
    pr.end_drawing()
    from OpenGL.GL import glFinish, glFlush
    glFlush()

pr.close_window()


