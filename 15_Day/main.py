MENU = {
    "espresso": {
        "ingredients":{
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water":200,
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
# print(MENU["espresso"]['ingredients']["water"])
value = 1
while value == 1:
    input_user = input(" What would you like? (espresso/latte/cappuccino):").lower()
    if input_user == "off":
        value=0
    elif input_user == "report":
        print(resources)
    elif input_user == "espresso":
        if MENU[input_user]["ingredients"]["water"] > resources["water"]:
            print("water is not enough")
        elif MENU[input_user]["ingredients"]["coffee"] > resources["coffee"]:
            print("coffee is not enough")
        else:
            resources["water"] = resources["water"] - MENU[input_user]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[input_user]["ingredients"]["coffee"]
            quarters = int(input("Insert coins:\nQuarters:"))
            dimes = int(input("dimes:"))
            nickel = int(input("nickel:"))
            pennies = int(input("pennies:"))
            total = float((quarters * 0.25) + (dimes * 0.10) + (nickel * 0.05) + (pennies * 0.01))
            total = round(total, 2)
            if total < MENU[input_user]["cost"]:
                print("Sorry that's not enough money")
            else:
                change = total - MENU[input_user]["cost"]
                print(f"Here is ${change} dollars in change")
                print(f"Here is your {input_user}. Enjoy!")
    elif input_user =="latte" or "cappuccino":
        if MENU[input_user]["ingredients"]["water"] > resources["water"]:
            print("water is not enough")
        elif MENU[input_user]["ingredients"]["coffee"] > resources["coffee"]:
            print("coffee is not enough")
        elif MENU[input_user]["ingredients"]["milk"] > resources["milk"]:
            print("milk is not enough")
        else:
            resources["water"] = resources["water"] - MENU[input_user]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU[input_user]["ingredients"]["coffee"]
            resources["milk"] = resources["milk"] - MENU[input_user]["ingredients"]["milk"]
