# import colorgram
#
# colors = colorgram.extract('Hirst Painting.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
from turtle import Turtle, Screen
from random import choice

color_list = [(192, 165, 115), (138, 166, 190), (56, 102, 140), (141, 91, 50), (12, 23, 55), (222, 207, 123),
              (182, 154, 42), (61, 22, 11), (182, 146, 165), (142, 177, 151), (72, 117, 81), (58, 15, 26),
              (126, 79, 102), (130, 30, 16), (15, 39, 23), (24, 53, 127), (177, 188, 215), (164, 104, 134),
              (115, 31, 46), (97, 150, 100), (98, 121, 172), (210, 178, 197), (174, 105, 93), (74, 150, 165),
              (25, 91, 65), (172, 205, 180)]

# It starts the artist and the canvas
Lentin = Turtle()
screen = Screen()
screen.colormode(255)
Lentin.speed("fastest")
Lentin.hideturtle()
Lentin.penup()

# The code below just puts the turtle in a better starting position
Lentin.forward(-300)
Lentin.right(90)
Lentin.forward(200)
Lentin.right(-90)


def paint_horizontal():
    for _ in range(10):
        Lentin.dot(20, choice(color_list))
        Lentin.forward(50)


def up():
    Lentin.right(-90)
    Lentin.forward(50)
    Lentin.right(-90)
    Lentin.forward(500)
    Lentin.right(180)


for _ in range(10):
    paint_horizontal()
    up()


screen.exitonclick()

