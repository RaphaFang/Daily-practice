from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_item()
    choice = input(f"What do you like like?({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                # if .make_payment() return T, which means it's match the cost
                coffee_maker.make_coffee(drink)

## 以更接近自然語言的方式，表達出條件，與前往下路徑
## 把複雜的部分外包成class