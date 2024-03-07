from turtle import Turtle, Screen
import random
timmy_T = Turtle()
timmy_T.shape("turtle")
timmy_T.color("red")
screen = Screen()

## 1.____________________________________________________
# for i in range(0, 4):
#     timmy_T.forward(100)
#     timmy_T.left(90)

## beaware not typing like "from turtle import *"
## which will import everything inside turtle modual,
    ## you will get confused about where the class come from? when dealing plenty of imports
## use "import turtle as t"
    ## "timmy = t.Turtle"
    ## "t" will be the rename of the file name

## 2.____________________________________________________
# for _ in range(15):
#     timmy_T.forward(10)
#     timmy_T.penup()
#     timmy_T.forward(10)
#     timmy_T.penudown()

## 3.____________________________________________________
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# for ankle in range(3, 9):
#     twist = 360/ankle
#     timmy_T.color(random.choice(colours))
#     for time in range(ankle):
#         timmy_T.forward(100)
#         timmy_T.right(twist)

## 4.____________________________________________________
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions =[0, 90, 180, 270]

# timmy_T.pensize(10)
# timmy_T.speed("fastest")
# for move in range(200):
#     timmy_T.color(random.choice(colours))
#     timmy_T.forward(20)
#     timmy_T.setheading(random.choice(directions))

## 5.____________________________________________________
## tuple, which is immutable, the value inside this listike set can't be change
## but you can change it by using, list(my_tuple)
# import turtle as t
# timmy_T = t.Turtle()
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# directions =[0, 90, 180, 270]
# timmy_T.pensize(10)
# timmy_T.speed("fastest")

# for move in range(200):
#     timmy_T.color(random_color)
#     timmy_T.forward(20)
#     timmy_T.setheading(random.choice(directions))


## 6.____________________________________________________
import turtle as t
timmy_T = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy_T.color(random_color())
        timmy_T.circle(100)
        timmy_T.setheading(timmy_T.heading() + size_of_gap)

timmy_T.speed("fastest")
draw_spirograph(1)

screen = t.Screen()
