from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        self.write(f"current score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def score_update(self):
        self.score +=1
        self.clear()
        self.write(f"current score: {self.score}", False, align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGNMENT, font=FONT)