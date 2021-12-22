from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

SCORE_COLOR = "LightBlue"
GAME_OVER_TEXT_COLOR = "Orange"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(SCORE_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", font= FONT, align=ALIGNMENT)

    def game_over(self):
        self.color(GAME_OVER_TEXT_COLOR)
        self.goto(0,0)
        self.write(arg="GAME OVER", font = FONT, align = ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
