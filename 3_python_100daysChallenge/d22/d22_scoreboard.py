from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_p1 = 0
        self.score_p2 = 0
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_p1, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_p2, align="center", font=("Courier", 80, "normal"))


    def add_p1(self):
        self.score_p1 +=1
        self.update_scoreboard()

    def add_p2(self):
        self.score_p2 +=1
        self.update_scoreboard()
