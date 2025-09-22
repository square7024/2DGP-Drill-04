from pico2d import *

open_canvas()

character = load_image('knight_animation_sheet.png')

while True:
    for i in range(3):
        draw_knight(i)
        delay(1)

close_canvas()