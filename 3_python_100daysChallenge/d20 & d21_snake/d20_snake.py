from turtle import Turtle
START_POSITION=[(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
## to declare like this is for future adjest easily

class Snake:
    def __init__(self):
        self.block_list=[]
        self.creat_snake()
        self.head = self.block_list[0]

    def creat_snake(self):
        for position in START_POSITION:
            self.tail(position)

    def tail(self, position):
        new_block = Turtle("turtle")
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        self.block_list.append(new_block)
    
    def add_tail(self):
        self.tail(self.block_list[-1].position())

    def move(self):
        for snake_move in range(len(self.block_list)-1, 0 ,-1):
            new_x = self.block_list[snake_move -1].xcor()
            new_y = self.block_list[snake_move -1].ycor()
            self.block_list[snake_move].goto(new_x, new_y)
        self.block_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)




