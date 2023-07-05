from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)

lumpik = Turtle()
lumpik.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def spirograph(gap):
    for x in range(int(360/gap)):
        lumpik.pencolor(random_color())
        lumpik.speed(40)
        lumpik.circle(70)
        lumpik.left(gap)

spirograph(1)

my_screen = Screen()
my_screen.exitonclick()