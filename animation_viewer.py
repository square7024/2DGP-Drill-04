from pico2d import *

open_canvas()

character = load_image('knight_animation_sheet.png')

frame = 0
start = 400

def draw_knight_walk():
    for frame in range(8):
        clear_canvas()
        character.clip_draw(frame*100 + start, 0, 200, 200, 400, 300)
        update_canvas()
        delay(0.1)
    pass


def draw_knight_run():
    pass


def draw_knight_attack():
    pass


def draw_knight_runattack():
    pass


def draw_knight(i):
    frame = 0
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