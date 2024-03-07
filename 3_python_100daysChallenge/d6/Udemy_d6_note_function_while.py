## https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# 1.____________________________________________________________
# def right():
#     turn_left()
#     turn_left()
#     turn_left()
# def loop():
#     move()
#     turn_left()
#     move()
#     right()
#     move()
#     right()
#     move()
#     turn_left()
        
# times = 0
# while not at_goal():
#     times += 1
#     if times == 1:
#         loop()
#         times -=1

## even batter way, 
# while not at_goal():
#     loop()
    
## the robot project, not in the py language
## if you want to check wether the conditon in while func. runs forever,
## you can add "print(5>3)", if it turns out "true" forever, then you got the bug.


# 2.____________________________________________________________
# def right():
#     turn_left()
#     turn_left()
#     turn_left()
# def up_and_down_loop():
#     turn_left()
#     move()
#     right()
#     move()
#     right()
#     move()
#     turn_left()
    
# a = 1
# while a>0:
#     if wall_in_front():
#         up_and_down_loop()
#     elif front_is_clear() and not at_goal():
#         move()
#     elif at_goal():
#         a = 0

# # the more clever way, 
# while not at_goal():
#     if wall_in_front():
#         up_and_down_loop()
#     else:
#         move()


# 3.____________________________________________________________
# def right():
#     turn_left()
#     turn_left()
#     turn_left()
# def up_and_down_loop():
#     turn_left()
#     while wall_on_right():
#         move()
#     right()
#     move()
#     right()
#     move()
#     while wall_on_right()and not wall_in_front():
#         move()
#     turn_left()
    
# while not at_goal():
#     if wall_in_front():
#         up_and_down_loop()
#     else:
#         move()

## solved in 5 mim!!!


# 4.____________________________________________________________
# def right():
#     turn_left()
#     turn_left()
#     turn_left()

# def start():
#     turn_time = 0
#     while not wall_on_right():
#         turn_left()
#         turn_time +=1
#         if turn_time == 4:
#             move()
#     while not wall_on_right():
#         turn_left()
                
# def follow_the_wall():
#     if right_is_clear() and front_is_clear():#右邊沒有，前面沒有
#         right()
#         move()
#     elif right_is_clear() and not front_is_clear():#右邊沒有，前面有
#         right()
#         move()
#     elif not front_is_clear() and not right_is_clear():#右邊有，前面有
#         turn_left()
#     elif not right_is_clear() and front_is_clear(): #右邊有，前面沒有
#         move()

# start()
# while not at_goal():
#     follow_the_wall()

# divide the question, 1.I need to deal the starting, 2.I need to deal the "follow the right wall" asign
## solved in 60 min