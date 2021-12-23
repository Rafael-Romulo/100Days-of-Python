from turtle import Turtle

PADDLE_COLOR = "LightBlue"

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(PADDLE_COLOR)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
