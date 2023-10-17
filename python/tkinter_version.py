from tkinter import *
from math import sin, cos, pi


# the turns and steps that the 'turtle' will make
fractal_angles  = []
fractal_lengths = []

# stroke width and color of the lines
LINE_WIDTH = 3
LINE_FILL = 'black'

# window height and width
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500

# main window and canvas of the fractal
root = Tk()
root.title("Interesting fractal")
C = Canvas(root, bg="white", height=WINDOW_HEIGHT, width=WINDOW_WIDTH)

def forward(l):
    fractal_angles.append(0)
    fractal_lengths.append(l)

# turns the 'turtle' right theta degrees
def right(theta):
    fractal_angles.append(theta * pi / 180)
    fractal_lengths.append(0)

# turns the 'turtle' left theta degrees
def left(theta):
    right(-theta)

# resets the turtle angles
def reset():
    global fractal_angles
    global fractal_lengths
    fractal_angles  = []
    fractal_lengths = []

def draw_all_steps(canvas, x, y):
    a, b = x, y
    theta = 0
    steps_len = len(fractal_lengths)
    for index in range(steps_len):
        angle =  fractal_angles [index]
        theta += angle
        length = fractal_lengths[index]
        a = x + length * cos(theta)
        b = y + length * sin(theta)
        canvas.create_line(x, y, a, b, fill=LINE_FILL, width=LINE_WIDTH)
        x = a
        y = b
    canvas.pack()
# Does one iteration of the fractal
# The whole picture consists of multiple iterations drawn over each other
def fractal_step(iter, l):
    if iter == 0:
        forward(l)
    else:
        new_l = l / 2
        new_iter = iter - 1
        left(90)
        fractal_step(new_iter, new_l)
        right(90)
        fractal_step(new_iter, new_l)
        right(90)
        fractal_step(new_iter, new_l)
        fractal_step(new_iter, new_l)
        left(90)
        fractal_step(new_iter, new_l)
        left(90)
        fractal_step(new_iter, new_l)
        right(90)

# draws the whole fractal
def draw_fractal(iter, length):
    for i in range(iter):
        reset()
        fractal_step(i, length)
        draw_all_steps(C, .5 * (WINDOW_WIDTH - length), .5 * WINDOW_HEIGHT)

draw_fractal(2, 100)

root.mainloop()