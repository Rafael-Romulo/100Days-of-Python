from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width = 800, height=520)
is_race_on = False

user_bet = screen.textinput(prompt = "Which turtle will win the race? Enter a color below", title = "Make a bet")

colors = ["blue", "red", "black", "green", "purple", "orange"]

competitors = []

def create_turtle(competitor,num_of_competitors):
    competitor = Turtle(shape = "turtle")
    competitor.shapesize(2)
    competitor.speed("fast")
    competitor.penup()
    color_of_player = random.choice(colors)
    competitor.color(color_of_player)
    colors.remove(color_of_player)
    competitor.goto(x = -370,y = (220-(num_of_competitors*80)))
    competitors.append(competitor)


FirstTurtle = Turtle(shape = "turtle")
FirstTurtle.shapesize(2)
FirstTurtle.speed("fast")
FirstTurtle.penup()
competitors.append(FirstTurtle)


num_of_rivals = 1


color_of_player = random.choice(colors)
FirstTurtle.color(color_of_player)
colors.remove(color_of_player)
FirstTurtle.goto(-370, 220)



for t in range(5):
    create_turtle(t, num_of_rivals)
    num_of_rivals +=1



if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in competitors:
        if turtle.xcor() > 380:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You've won the bet! The {winning_color} turtle was the fastest! ")
            else:
                print(f"You've lost. The {winning_color} turtle was the fastest! ")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()
