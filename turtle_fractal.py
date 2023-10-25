from turtle import *

# Does one iteration of the fractal
# The whole picture consists of multiple iterations drawn over each other
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

# Draws 'iter' iterations of the fractal stacked on each other
def draw_fractal(iter, l):
    speed('fastest')
    penup()
    goto(-.5 * l, 0)
    for i in range(iter+1):
        pendown()
        draw_fractal_step(i, l)
        penup()
        goto(-.5 * l, 0)

# The length and number of iterations of the fractal
iterations = 3
length = 300


draw_fractal(iterations, length)
done()