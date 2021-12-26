from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

SCORE_COLOR = "LightBlue"
GAME_OVER_TEXT_COLOR = "Orange"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.color(SCORE_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", font= FONT, align=ALIGNMENT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            with open("data.txt", "w") as HS:
                HS.write(f"{self.score}")

        self.score = 0
        self.update_scoreboard()