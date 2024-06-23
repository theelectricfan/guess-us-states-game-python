import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.bgpic("./blank_states_img.gif")

states_data = pandas.read_csv("./50_states.csv")

states = states_data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    titlecase_answer = answer.title() if answer else None

    if answer == "Exit" or answer is None:
        states_to_learn = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states_data[states_data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer, align="center", font=("Arial", 8, "normal"))


screen.exitonclick()