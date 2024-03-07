# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move():
#     tim.forward(10)
    

# screen.listen()
# screen.onkey(key="space", fun=move)
# screen.exitonclick()


##__________________________________________________________
## higher order function, take 



## 1. __________________________________________________________
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move():
    tim.forward(10)

def backward():
    tim.backward(10)

# tim.setheading(180)
# inprivious, i use only the setheading() func, which will only "set" the heading as input
    # e.g. set heading as 180
    # it won't 'change' the func, while keep using this func
def clockwise():
    new_heading = tim.heading() +10
    tim.setheading(new_heading)

def counter_clockwise():
    new_heading = tim.heading() -10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move)
screen.onkey(key="s", fun=backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)


screen.exitonclick()







