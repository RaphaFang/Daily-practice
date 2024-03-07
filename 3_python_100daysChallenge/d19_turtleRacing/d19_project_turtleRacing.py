from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(500, 400)

on_race = False

userbet = screen.textinput("make your bet.", "Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_p = [-70, -40, -10, 20, 50, 80]
all_t =[]

for turtle_index in range(0,6):
    turtle_each = Turtle(shape= "turtle")
    turtle_each.color(color[turtle_index])
    turtle_each.penup()
    turtle_each.goto(x=-240, y=y_p[turtle_index])
    all_t.append(turtle_each)

if userbet:
    on_race = True

while on_race:
    for turtle in all_t:
        ran_distance = random.randint(0, 10)
        turtle.forward(ran_distance)
        if turtle.xcor() >230:
            on_race = False
            winner_color = turtle.pencolor()
            if userbet == winner_color:
                print(f"You've won! The {winner_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winner_color} turtle is the winner!")

screen.exitonclick()