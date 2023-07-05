from turtle import Turtle, Screen

lumpik = Turtle()

colors = ["red", "blue"]
bigger = 10

for x in range(12):
    if x == 0:
        lumpik.pencolor("red")
    else:
        lumpik.pencolor("blue")
    lumpik.circle(bigger)
    bigger += 10

screen = Screen()
screen.exitonclick()