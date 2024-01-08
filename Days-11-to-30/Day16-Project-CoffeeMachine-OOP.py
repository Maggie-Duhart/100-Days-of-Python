MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money = 0.0


def check_resources(order_ingredients):
    """Returns True if we can make the order or False if ingredients are not enough"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True


def insert_payment():
    print("Please insert coins")
    quarters = int(input("how many quarter?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    total_quarter = quarters * 0.25
    total_dimes = dimes * 0.10
    total_nickles = nickles * 0.05
    total_pennies = pennies * 0.01

    total_paid = total_quarter + total_dimes + total_nickles + total_pennies

    return total_paid


def transaction_succeed(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refund")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


ordering = True


while ordering:
    select = input("  What would you like? (espresso/latte/cappuccino): ").lower()
    if select == "off":
        ordering = False
    elif select == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        coffe_style = MENU[select]
        if check_resources(coffe_style["ingredients"]):
            payment = insert_payment()
            if transaction_succeed(payment, coffe_style["cost"]):
                make_coffee(select, coffe_style["ingredients"])

