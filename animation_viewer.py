from pico2d import *

open_canvas()

character = load_image('knight_animation_sheet.png')

def draw_knight(i):
    if (i == 0): draw_knight_walk()
    elif (i == 1): draw_knight_run()
    elif (i == 2): draw_knight_attack()
    elif (i == 3): draw_knight_runattack()
    pass

while True:
    for i in range(3):
        draw_knight(i)
        delay(1)

close_canvas()