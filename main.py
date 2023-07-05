from turtle import Turtle, Screen

strany = 4

tommy = Turtle()
tommy.shape("turtle")

while tommy:
    tommy.forward(50)
    tommy.left(90)
    strany -= 1
    if strany == 0:
        break

#pro for:
#for x in range(0, 4):
#    tommy.forward(50)
#    tommy.left(90)

my_screen = Screen()
my_screen.exitonclick()