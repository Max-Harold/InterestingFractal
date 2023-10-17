from shutil import move
from turtle import *

def draw_fractal_step(iter, l):
    if iter == 0:
        forward(l)
    else:
        new_l = l / 2
        new_iter = iter - 1
        left(90)
        draw_fractal_step(new_iter, new_l)
        right(90)
        draw_fractal_step(new_iter, new_l)
        right(90)
        draw_fractal_step(new_iter, new_l)
        draw_fractal_step(new_iter, new_l)
        left(90)
        draw_fractal_step(new_iter, new_l)
        left(90)
        draw_fractal_step(new_iter, new_l)
        right(90)


def draw_fractal(iter, l):
    speed(0)
    penup()
    goto(-l, 0)
    for i in range(1, iter+1):
        pendown()
        draw_fractal_step(i, l)
        penup()
        goto(-l, 0)
draw_fractal(5, 300)
done()