from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


if __name__ == "__main__":
    loops = True
    menu_object = Menu()
    mm_object = MoneyMachine()
    cm_object = CoffeeMaker()
    while loops:
        choice = input("What would you like? ({}):".format(menu_object.get_items()))
        if choice == 'report':
            print(mm_object.report())
            print(cm_object.report())
        elif choice == 'off':
            loops = False
        else:
            if cm_object.is_resource_sufficient(menu_object.find_drink(choice)):
                if mm_object.make_payment(menu_object.find_drink(choice).cost):
                    cm_object.make_coffee(menu_object.find_drink(choice))