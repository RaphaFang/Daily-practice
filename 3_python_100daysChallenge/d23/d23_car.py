COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(COLORS[random.randint(0,5)])
        self.penup()
        self.x_move = MOVE_INCREMENT
        self.move_speed = 0.1
        
    
    def genecar(self):
        self.startig_y = random.randint(-280,280)

    def move(self):
        self.genecar()
        new_x = self.xcor() - self.x_move
        self.goto(new_x, self.startig_y)


    def reset_speedup(self):
        self.clear()
        self.move_speed *= 0.9



