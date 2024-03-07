import time
from turtle import Screen
from d23_player import Player
from d23_car import CarManager
from d23_scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "s")
screen.onkey(player.go_left, "a")
screen.onkey(player.go_right, "d")


game_is_on = True
while game_is_on:
    time.sleep(car.move_speed)
    screen.update()
    car.move()
    # while player.ycor()< 280:
    
    if player.ycor()> 280:
        ## car reset
     ## car speed up
        player.back_position()
        scoreboard.add_score()
        car.reset_speedup()
    # if 
    #     game_is_on = False
    #     scoreboard.you_loss()

screen.exitonclick()