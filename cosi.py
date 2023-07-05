from turtle import Turtle, Screen
import random

angle = 360
moves = 3

tommy = Turtle()
tommy.shape("turtle")

colors = ["azure2", "brown4", "chartreuse", "coral1", "cornsilk2", "DarkMagenta", "DarkSeaGreen3", "DeepSkyBlue4"]

while moves != 20:
    random_color = random.choice(colors) #náhodný výběr z listu colors
    tommy.pencolor(random_color)
    for x in range(moves):
        tommy.forward(40)
        tommy.right(360/moves)
    moves += 1

my_screen = Screen()
my_screen.exitonclick()