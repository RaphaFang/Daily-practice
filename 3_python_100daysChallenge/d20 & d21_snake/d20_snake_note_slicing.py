# from turtle import Turtle, Screen
# from d20_snake import Snake
# import time

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.title("My Snake Game")
# screen.bgcolor("black")
# screen.tracer(0)

# start_position =[(0,0), (-20,0), (-40,0)]
# # for _ in range(0,3):
# #     _ = Turtle("square")
# #     _.color("white")
# #     _.goto(start_position[int(_)], 0)

# ## can't use _ in for loop as interger

# block_list=[]
# for position in start_position:
#     new_block = Turtle("square")
#     new_block.color("white")
#     new_block.penup()
#     new_block.goto(position)
#     block_list.append(new_block)

# # screen.update()
# game_on = True
# while game_on:
#     screen.update()
#     time.sleep(0.1)
#     for snake_move in range(len(block_list)-1, 0 ,-1):
#         new_x = block_list[snake_move -1].xcor()
#         new_y = block_list[snake_move -1].ycor()
#         block_list[snake_move].goto(new_x, new_y)
#     ## beaware that, how the list placed, they placed [0](0,0), [1](-20,0), [2](-40,0)
#         ## as a result, [2] should move to [1]
#     block_list[0].forward(20)

# screen.exitonclick()

## _----------------------------------------------------- 
# slicing

piano = ['a','b', 'c','d', 'e']
# print(piano[a:b:c])
# a for start
# b for end
# c for skip, input 2, means skip the each second element
#      if c input "-1", it reverse the list
print(piano[2:5])

print(piano[1:-1])
# it will gives you 2 3 4 , but without the first & last one

print(piano[1:])