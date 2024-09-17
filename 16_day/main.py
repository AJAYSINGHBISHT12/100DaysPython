from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
on = 1
drink = Menu()
CoffeTemplate = CoffeeMaker()
MoneyM = MoneyMachine()
while on == 1:
    x = input("What would you like? (espresso/latte/cappuccino/):").lower()
    if x == "off" :
        on = 0
    elif x == "report":
        CoffeTemplate.report()
    elif x == "espreso" or "latte" or "cappuccino":
        y = drink.find_drink(x)
        cost = y.cost
        if CoffeTemplate.is_resource_sufficient(y) == True:
            if MoneyM.make_payment(cost) == True:
                CoffeTemplate.make_coffee(y)

