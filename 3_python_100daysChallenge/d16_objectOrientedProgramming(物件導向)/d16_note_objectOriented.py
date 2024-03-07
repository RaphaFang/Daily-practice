## the things that object has is "attributes"
## the func. object do is "methods", model by functions

## class and object

# from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color("white")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvaheight)
# my_screen.exitonclick()


from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon name", ["a","b"])
table.add_column("Type", ["a","b"])
## table[0].align("r")  incorrect
table.align = "l"

print(table)
