from turtle import Screen
from d22_paddle import Paddle
from d22_ball import Ball
from d22_scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle_p1 = Paddle((350, 0))
paddle_p2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_p1.go_up, "Up")
screen.onkey(paddle_p1.go_down, "Down")
screen.onkey(paddle_p2.go_up, "w")
screen.onkey(paddle_p2.go_down, "s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() >280 or ball.ycor() <-280:
        ball.bounce_x()
    if (ball.distance(paddle_p2) <50 and ball.xcor() < -340) or (ball.distance(paddle_p1) <50 and ball.xcor() > 340):
        ball.bounce_y()
        ## 前面寫錯 paddle_p1 paddle_p2 的xcor()，導致我以為「連續彈跳」是因為，即便球與板子的距離因為bounce_y()增加
        ## 仍符合<50，以及<-340，因此會連續彈跳。
        ## 實際情況，寫對 xcor()，在第一次彈跳就會超過<-340的要求


    if ball.xcor() >380:
        ball.reset_ball()
        scoreboard.add_p1()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.add_p2()




screen.exitonclick()