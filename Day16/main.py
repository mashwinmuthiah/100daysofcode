from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    loops = True
    menu = Menu()
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    while loops:
        choice = input("What would you like? ({}):".format(menu.get_items()))
        if choice == 'report':
            coffee_maker.report()
            money_machine.report()
        elif choice == 'off':
            loops = False
        else:
            if coffee_maker.is_resource_sufficient(menu.find_drink(choice)):
                if money_machine.make_payment(menu.find_drink(choice).cost):
                    coffee_maker.make_coffee(menu.find_drink(choice))
