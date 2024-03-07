from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')
str = "/Users/fangsiyu/Desktop/program/3_python_100daysChallenge/d24_hightScore_mailMerge/snake_data.txt"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.score = 0
        with (str) as data:
            self.hightscore = int(data.read())
        self.write(f"current score: {self.score}", False, align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"current score: {self.score} High Score: {self.hightscore}", False, align="center", font=FONT)

    def reset(self):
        if self.score> self.hightscore:
            self.hightscore = self.score
            with open(str, mode='w') as data:
                data.write(f'{self.hightscore}')
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align=ALIGNMENT, font=FONT)