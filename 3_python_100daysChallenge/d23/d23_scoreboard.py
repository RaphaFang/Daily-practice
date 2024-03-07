FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.cross_score = 0
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 250)
        self.write(self.cross_score, align="center", font=("Courier", 24, "normal"))

    def add_score(self):
        self.cross_score +=1
        self.update_scoreboard()

    def you_loss(self):
        self.clear()
        self.goto(0, 200)
        self.write("You Loss\nScore:{self.cross_score}", align="center", font=("Courier", 24, "normal"))