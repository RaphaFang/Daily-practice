import pandas
import turtle

screen = turtle.Screen()
screen.title("USA map game")
image = "3_python_100daysChallenge/d25_data/d25_USAmap/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("3_python_100daysChallenge/d25_data/d25_USAmap/50_states.csv")
state_name = data.state.to_list()
guessed_states = []

# print(state_name)

while len(guessed_states)< 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states", 
                                prompt= "What's another stakes name?").title()
## title(), gives the first letter uppercase
    if answer_state == "Exit":
        learning_list = [n for n in state_name if n not in guessed_states]

        # learning_list = []
        # for n in state_name:
        #     if n not in guessed_states:
        #         learning_list.append(n)
        df = pandas.DataFrame(learning_list)
        df.to_csv("learning_list.csv")
        
        break
        

    if answer_state in state_name:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
    ## .item() give you the first item of the row
        t.write(state_data.state.item())
    ## write below would be fine
        t.write(answer_state)