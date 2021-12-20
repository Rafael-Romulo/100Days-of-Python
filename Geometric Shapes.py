from turtle import Screen, Turtle
from random import random


screen = Screen()
Lentin = Turtle()
Lentin.speed("fastest")
Lentin.hideturtle()

answer = int(screen.textinput(title = "Geometry", prompt= "Type any number above 3")) + 1

def change_color(turtle):
    r = random()
    g = random()
    b = random()
    random_color = (r, g, b)
    turtle.color(random_color)


def draw(sides):
    for _ in range(sides):
        Lentin.forward(80)
        Lentin.right(360- 360/sides)
        Lentin.end_fill()


for i in range(3, answer):
    change_color(Lentin)
    draw(i)


screen.exitonclick()
