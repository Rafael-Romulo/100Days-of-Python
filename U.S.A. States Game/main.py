import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()

already_guessed = []

count = 0

guess = screen.textinput(title="Try and guess the State", prompt="What is another state`s name?").title()

while count != 50:
    if guess == "Exit":
        missing_states = []
        for state in all_states:
            if state not in already_guessed:
                missing_states.append(state)
        newData = pandas.DataFrame(missing_states)
        newData.to_csv("Missing States.csv")
        break

    if guess in already_guessed:
        guess = screen.textinput(title=f"{count}/50 States Correct", prompt="You`ve already guessed that.\nWhat is another state`s name?").title()

    elif guess in all_states:
        new_t = turtle.Turtle()
        new_t.hideturtle()
        new_t.penup()
        state_data = data[data.state == guess]
        new_t.goto(int(state_data.x), int(state_data.y))
        new_t.write(guess)
        count+=1
        already_guessed.append(guess)
        guess = screen.textinput(title=f"{count}/50 States Correct",
                                 prompt="Nice, you got it right!\nWhat is another state`s name?").title()
    else:
        guess = screen.textinput(title=f"{count}/50 States Correct",
                                 prompt="You guessed wrong. Try again.\nWhat is another state`s name?").title()




screen.exitonclick()