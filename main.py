import turtle,pandas as pd

import pandas

# from s_name import StateName

screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.bgpic(image)
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data.state.to_list()

guessed_states = []
# answer = screen.textinput(f"{score}/50 States Correct", "What's the name of the state?")
while len(guessed_states) < 50:
    answer = screen.textinput(f"{len(guessed_states)}/50 States Correct","What's the name of the state?").title()
    if answer == "Exit":
        new_data = pandas.DataFrame(states)
        new_data.to_csv("Remaining_States.csv")
        break
    if answer in states and answer not in guessed_states:
        guessed_states.append(answer)
        states.remove(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # t.color("Black")
        state_data = data[data.state == answer]
        t.goto(int(state_data.x.item()),int(state_data.y.item()))
        t.write(answer)












screen.exitonclick()