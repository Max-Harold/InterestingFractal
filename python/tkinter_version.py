from tkinter import *
from math import sin, cos, pi


# the turns and steps that the 'turtle' will make
fractal_angles  = []
fractal_lengths = []

# stroke width and color of the lines
LINE_WIDTH = 1
LINE_FILL = 'black'

# length and iterations of the fracta
FRACTAL_LENGTH = 300
prev_iters = 1


# window height and width
WINDOW_HEIGHT = 750
WINDOW_WIDTH = 750

# main window and canvas of the fractal
root = Tk()
root.title("Interesting fractal")
C = Canvas(root, bg="white", height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
C.pack()
ITERATIONS = IntVar(value=1)


scale_widget = Scale(root, from_=1, to=7,
                             orient=HORIZONTAL,
                             length=500, variable=ITERATIONS)

scale_widget.set(1)
scale_widget.pack()

def reset_fractal():
    global prev_iters
    if prev_iters != ITERATIONS.get():
        C.delete('all')
        draw_fractal(ITERATIONS.get(), FRACTAL_LENGTH)
        prev_iters = ITERATIONS.get()
    root.after(10, reset_fractal)
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
        draw_all_steps(C, .5 * (WINDOW_WIDTH - length), .5 * (WINDOW_HEIGHT))

draw_fractal(ITERATIONS.get(), FRACTAL_LENGTH)
root.after(10, reset_fractal)
root.mainloop()