from turtle import Turtle, Screen
import random
import turtle

colors = ["red", "blue", "green", "pink", "yellow", "brown", "orange", "purple"]

lumpik = Turtle()
lumpik.speed(20)
lumpik.pensize(3)
long = 0.5

for x in range(0, 300):
    lumpik.pencolor(colors[x%8])
    lumpik.forward(x)
    lumpik.right(80)

my_screen = Screen()
my_screen.exitonclick()