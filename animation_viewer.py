from pico2d import *

open_canvas()

character = load_image('knight_animation_sheet.png')

frame = 0
start = 310

def draw_knight_walk():
    for i in range(5):
        print("knight_walk", i)
        for frame in range(8):
            clear_canvas()
            if frame <= 4:
                character.clip_draw(frame*100 + start, 610, 90, 100, 400, 300)
            if frame > 4 and frame < 6:
                character.clip_draw(frame * 100 + start - 10, 610, 90, 100, 400, 300)
            if frame >= 6:
                character.clip_draw(frame * 100 + start - 20, 610, 90, 100, 400, 300)
            update_canvas()
            delay(0.5)
    pass


def draw_knight_run():
    for i in range(5):
        print("knight_run", i)
        for frame in range(7):
            clear_canvas()
            character.clip_draw(frame*100 + start, 480, 90, 100, 400, 300)
            update_canvas()
            delay(0.35)
    pass


def draw_knight_attack():
    for i in range(5):
        print("knight_attack", i)
        for frame in range(5):
            clear_canvas()
            if frame < 4:
                character.clip_draw(frame * 110 + start, 180, 100, 130, 400, 300)
            if frame == 4:
                character.clip_draw(frame * 110 + start, 180, 200, 130, 450, 300)
            update_canvas()
            delay(0.15)
    pass


def draw_knight_runattack():
    for frame in range(6):
        clear_canvas()
        if frame < 4:
            character.clip_draw(frame * 100 + start, 320, 110, 140, 400, 300)
        if frame == 4:
            character.clip_draw(frame * 100 + start + 10, 320, 110, 140, 400, 300)
        if frame == 5:
            character.clip_draw(frame * 100 + start + 20, 320, 110, 140, 400, 300)
        update_canvas()
        delay(0.15)
    pass


def draw_knight(i):
    frame = 0
    if (i == 0): draw_knight_walk()
    elif (i == 1): draw_knight_run()
    elif (i == 2): draw_knight_attack()
    elif (i == 3): draw_knight_runattack()
    pass

while True:
    # for i in range(3):
        draw_knight(3)
        delay(1)

close_canvas()