from turtle import Turtle

FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260, 240)
        self.color("Purple")
        self.write(f"Stage: {self.level}", align="left", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Stage: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.color("Black")
        self.write("Game Over", align="center", font=FONT)
