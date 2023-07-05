from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

lumpik = Turtle()
lumpik.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

angles = [90, 180, 270]
directions = [10, 15]
#colors = ["blue", "red", "green", "yellow", "brown", "orange"]

for x in range(0, 500):
    rr_angle = random.choice(angles)
    rl_angle = random.choice(angles)
    r_direction = random.choice(directions)
    #r_color = random.choice(colors)

    if x <= 7:
        lumpik.pensize(x)

    lumpik.pencolor(random_color())
    lumpik.forward(r_direction)
    lumpik.right(rr_angle)
    lumpik.left(rl_angle)

my_screen = Screen()
my_screen.exitonclick()