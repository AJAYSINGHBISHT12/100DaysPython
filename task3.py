# #Condition statements
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
#
# if height > 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")
#
# print(10%5)
# if(int(input("Please provide the number"))%2==0):
#     print("it i divisible by 2")
# else:
#     print("Not divisible by 2")
# bill = 0
# print("Welcome to the Python Pizza Deliveries!")
# size = input("What size pizza do you want? S,M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
# if(size == "S"):
#     bill += 15
# elif(size == "M"):
#     bill +=20
# elif(size == "L"):
#     bill +=25
# else:
#     print("you typed the wrong inputs")
#
# if(pepperoni == "Y"):
#     if(size == "S"):
#         bill +=2
#     else:
#         bill +=3
#
# if(extra_cheese == "Y"):
#     bill+=1
# print(f"your final bill is: ${bill}"# )
print("Welcome to the Treasure Island. Your mission is to find the treasure")
y=input("Select Left or right").lower()
if(y== "right"):
    print("Game Over")
elif(y=="left"):
    x=input("Swim or wait").lower()
    if(x=="swim"):
        print("Game Over")
    elif(x=="wait"):
        z=input("Which door").lower()
        if(z=="yellow"):
            print("You Win")
        elif(z=="red" or z=="blue"):
            print("Game Over")