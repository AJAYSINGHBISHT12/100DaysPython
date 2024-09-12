#This is the task of the day2
#Subscripting
# print("Hello"[-2])
# #Concatenation[String]
# print("123"+"345")
# #Integer
# print(123+345)
# print(123_345_566)
# #float
# print(3.14244)
# #Boolean
# # print(True)
# # print(False)
# len("Hello")
# #Type-checking
# print(type("123"),type(123),type(123.8),type(True))
# #type-conversion
# print(int("123")+int("456"))
# print("a")
# print(4**2)
#PEMDASLR
#()
#**
# * OR /
# + OR -
# print(3 * 3 + 3 / 3 -3)
# score = 0
# score +=1
# score *=2
# print(score)
# #f-strings
#print("Your score is " + str(score))
# score = 0
# height = 1.8
# is_winning = True
# print(f"Your score is = {score}, your height is {height}, you are winning is {is_winning}")
# print(6 + 4 / 2 - (1 * 2))
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
number_of_people = input("How many people to split the bill?")
bill_per_with_tip = float(total_bill) + float((float(total_bill) * float((float(tip)**-2))))
bill_per_person = (float(bill_per_with_tip) / float(number_of_people))
result = round(bill_per_person , 2)
print(f"Each person should pay: $ {result}")