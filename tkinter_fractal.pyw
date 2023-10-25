from tkinter import *
from math import sin, cos, pi


# the turns and steps that the 'turtle' will make
all_fractal_angles  = {}
all_fractal_lengths = {}
fractal_angles = []
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

# Text that indicates the iterations modifier
iterations_text = Label(root, text="Iterations:")
iterations_text.config(font=("Courier", 14))
iterations_text.pack()

# the number of iterations the user desires
ITERATIONS = IntVar(value=0)

# the widget that allows the user to change the number of iterations of the fractal
iteration_modifier = Scale(root, from_=0, to=6,
                             orient=HORIZONTAL,
                             length=600, variable=ITERATIONS)

iteration_modifier.set(0)
iteration_modifier.pack()

# periodic function that checks if scale widget value has changed
def reset_fractal():
    global prev_iters
    if prev_iters != ITERATIONS.get():
        if prev_iters > ITERATIONS.get():
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

# resets the turtle angles and ensures that the path for the desired iteration is only generated once 
# and stored in all_fractal_angles and all_fractal_lengths
def reevaluate(iter, length):
    global all_fractal_angles
    global all_fractal_lengths
    global fractal_angles
    global fractal_lengths
    if iter not in all_fractal_angles:
        fractal_lengths = []
        fractal_angles = []
        fractal_step(iter, length)
        all_fractal_angles[iter] = fractal_angles
        all_fractal_lengths[iter] = fractal_lengths
    fractal_lengths = all_fractal_lengths[iter]
    fractal_angles = all_fractal_angles[iter]

# draws all the steps present in fractal_angles and fractal_lines
def draw_all_steps(canvas, x, y):
    global fractal_angles
    global fractal_lengths
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
    for i in range(iter+1):
        reevaluate(i, length)
        draw_all_steps(C, .5 * (WINDOW_WIDTH - length), .5 * (WINDOW_HEIGHT))

draw_fractal(ITERATIONS.get(), FRACTAL_LENGTH)
root.after(10, reset_fractal)
root.mainloop()