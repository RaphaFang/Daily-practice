from turtle import Turtle, Screen
from d20_snake import Snake
from d20_food import Food
from d20_scoreBoard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, key="w")
screen.onkey(snake.down, key="s")
screen.onkey(snake.right, key="d")
screen.onkey(snake.left, key="a")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) <15:
        food.refesh()
        snake.add_tail()
        scoreboard.score_update()
        
    if snake.head.xcor() > 290 or snake.head.xcor() <-290 or snake.head.ycor() >290 or snake.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()
    
    for snake_body in snake.block_list[1:-1]:
        if snake.head.distance(snake_body) < 10 :
            game_on = False
            scoreboard.game_over()

screen.exitonclick()