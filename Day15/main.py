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
    "money": 0
}


def menu():
    print("\t\t\t\t\t\t\t\t\t MENU")
    for i in MENU:
        print("\t\t\t\t\t\t\t\t {} - {}$".format(i, MENU[i]['cost']))
    choice_local = input("What would you like? (espresso/latte/cappuccino): ")
    return choice_local


def coffee(choice_local):
    print("Please Insert coins")
    q = float(input("How Many Quarters? "))
    d = float(input("How Many Dimes? "))
    n = float(input("How Many Nickles? "))
    p = float(input("How Many Pennies? "))
    total_input_coin = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    if choice_local in ['espresso', 'latte', 'cappuccino'] and total_input_coin >= MENU[choice_local]['cost']:
        resources["money"] += MENU[choice_local]['cost']
        for i in MENU[choice]['ingredients']:
            resources[i] -= MENU[choice]['ingredients'][i]
        print("Here is ${} in change.".format(total_input_coin - MENU[choice_local]['cost']))
        print("Here is your {} ☕️. Enjoy!".format(choice_local))
    else:
        print("Sorry that's not enough money. Money refunded.")


if __name__ == "__main__":
    loops = True
    while loops:
        choice = menu()
        if choice == 'report':
            for i in resources:
                if i == 'coffee':
                    print("{}: {}g".format(i, resources[i]))
                elif i == 'money':
                    print("{}: {}$".format(i, resources[i]))
                else:
                    print("{}: {}ml".format(i, resources[i]))
        elif choice == 'off':
            loops = False
        else:
            coffee_flag = True
            for i in MENU[choice]['ingredients']:
                if resources[i] < MENU[choice]['ingredients'][i]:
                    print("Sorry there is not enough {}.".format(i))
                    coffee_flag = False
                    break
            if coffee_flag : coffee(choice)
