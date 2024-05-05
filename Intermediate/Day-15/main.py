###### Coffee Machine simulator program #######

from art import logo
from IPython.display import clear_output


MENU = {
    "espresso": {
        "ingredients": {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def verify_resources (coffee):
    enough_resources = True
    message = "Sorry there is not enough: "
    for item in coffee:
        if coffee[item] > resources [item]:
            message = message + f" {item}."
            enough_resources = False
    
    if not enough_resources:
        print (message)
    
    return enough_resources


def verify_payment (money_paid, coffee_price, menu_option):
    total_paid = 0
    coins = {"quarters": 0.25, "dimes": .10, "nickels": 0.05, "pennies": 0.01}
    for key in money_paid:
        total_paid += money_paid [key] * coins [key]
    
    if total_paid < coffee_price:
        print ("Sorry that's not enough money. Money refunded.")
        return 0
    else:
        print (f"Here is ${round(total_paid - coffee_price, 2)} in change.")
        print (f"Here is your {menu_option} ☕. Enjoy!")
        return coffee_price


def report (money_in_machine):
    print (f"Water: {resources['water']}ml")
    print (f"Milk: {resources['milk']}ml")
    print (f"Coffee: {resources['coffee']}g")
    print (f"Money: ${money_in_machine}")


def receive_payment():
    coins_received = {"quarters": 0, "dimes": 0, "nickels": 0, "pennies": 0}
    for coin in coins_received:
        coins_received [coin] = int(input(f"how many {coin}?: "))

    return coins_received



keep_working = True
machine_money = 0
#print (logo)

while keep_working:
    coins_paid = {}
    user_option = input ("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_option == "report":
        report (machine_money)
    elif user_option == "off":
        break
    elif user_option in MENU:
        keep_working = verify_resources (MENU[user_option]["ingredients"])
        if keep_working:
            coins_paid = receive_payment ()
            money = verify_payment (coins_paid, MENU[user_option]["cost"], user_option)
            if money != 0:
                machine_money += money
                for item in MENU [user_option]["ingredients"]:
                    resources [item] -= MENU [user_option]["ingredients"][item]
    else:
        print ("Wrong coffee chosen. Try again!")
