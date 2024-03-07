## a term define "inside" the function, called local. ouside called global
## if you create a varible inside a function(local), 
## the way to avaliable call that var, is inside the function.

## so, it's possible to have 2 var call the same name, but have diffrernt value
## but, the variable inside a if function, it won't bound the var

## you can modified a var inside a def function, by adding "global" infront
## but avoide using this
## as alternative use "return" to add 1 to your global value

## the way to define a variable global & local, is to type it in "uppercase"
# def a_function(a_parameter):
#     a_variable = 15
#     return a_parameter
 
# a_function(10)
# print(a_variable)




globvar = 10

def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar -= 1
    print(globvar)

def print_globvar():
    print(globvar)     # No need for global declaration to read value of globvar

set_globvar_to_one()  # Prints 9
print_globvar()       # Prints 9

## it's wired that you can use the global var, by func only include print()
## if the var being used beside print(), you have to add "global" infront
URL = "https://stackoverflow.com/questions/423379/how-to-use-a-global-variable-in-a-function"