MENU = {
    "espresso": {
        "ingredients": {
            "milk":0,
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
coffee_cost = 0
input_money = 0
change = 0
chosen_coffee = ""
ingredients = [250, 200, 200]
keep_going = True

## check point
# print(type(ingredients[0]))
# print(type(MENU['cappuccino']['ingredients']['water']))

def select_coffee():
    global chosen_coffee
    print("Here's the price for each coffee.\nespresso: $1.5, latte: $2.5, cappuccino: $3.0")
    chosen_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if chosen_coffee == 'espresso' or chosen_coffee == 'latte' or chosen_coffee == 'cappuccino':
        return chosen_coffee
    else:
        return ("error coffee input")

def cost_and_ingredient():
    global coffee_cost
    if chosen_coffee == "espresso":
        coffee_cost = float(MENU['espresso']['cost'])
    elif chosen_coffee == "latte":
        coffee_cost = float(MENU['latte']['cost'])
    elif chosen_coffee == "cappuccino":
        coffee_cost = float(MENU['cappuccino']['cost'])
    return float(coffee_cost)

def ingredients_check():
    global keep_going
    if int(MENU[chosen_coffee]['ingredients']["water"]) > ingredients[0]:
        print("Sorry there is not enough water.")
        keep_going = False
    elif int(MENU[chosen_coffee]['ingredients']["milk"]) > ingredients[1]:
        print("Sorry there is not enough milk.")
        keep_going = False
    elif int(MENU[chosen_coffee]['ingredients']["coffee"]) > ingredients[2]:
        print("Sorry there is not enough coffee.")
        keep_going = False

# select_coffee()
# print(chosen_coffee)

def insert_coins():
    global input_money
    print("Please insert coins.")
    quarter = float(input("how many quarters?: "))*0.25
    dime = float(input("how many dimes?: "))*0.1
    nickle = float(input("how many nickles?: "))*0.05
    pennie = float(input("how many pennies?: "))*0.01
    input_money = float(quarter + dime + nickle + pennie)

def comparing():
    global MENU
    global input_money
    global keep_going
    if input_money >= coffee_cost:
        ingredients[0] -= int(MENU[chosen_coffee]['ingredients']['water'])
        ingredients[1] -= int(MENU[chosen_coffee]['ingredients']['milk'])
        ingredients[2] -= int(MENU[chosen_coffee]['ingredients']['coffee'])
        change = round(input_money - coffee_cost , 2)
        print(f"Here is ${change} in change.")
        print(f"ingredients remained, water:{ingredients[0]} milk:{ingredients[1]} coffee:{ingredients[2]}")
        print(f"Here is your {chosen_coffee} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
        keep_going = False

while keep_going:
    select_coffee()
    cost_and_ingredient()
    ingredients_check()
    if keep_going:
        insert_coins()
        comparing()
    

## 處理餘額問題 猜測 global           (O)
## 小數點問題 round   (O)
## 多設置一個檢測環節 連動到一變數T or F，決定最下方while的啟動  (O)
## 處理材料變成負數後，無法立刻離開while loop  (O)
        
## 潔敏，新開檔案處理更快速的開發
    ## for loop, func變數, 將ingredients轉變成字典
        

## 今天學到的，如果沒有透過global 將常數匯入自訂func.，自訂功能跑完後，下一個自訂功能會讀到原先的空白常數（coffee_cost = 0），並非跑完func.之後的常數
## for loop 填入的代數，兩側要是相同的。例如：abc[n] def[n] ,兩側要可以填入相同物件，而非一邊數值，一邊陣列中的物件
## while loop 如何在一長串指令中停止？ 透過在斷點處加入if 檢查。不然中間while值已經是Ｆ，但是尾巴一大串還沒跑完
        
## 今天的成就，學會透過 def func 切開編寫過程，但是在如何運用功能的值，帶入下一則功能，需要更多練習。
        ## while loop 如何中斷也需要練習（有沒有更漂亮的）