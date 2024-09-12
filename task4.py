import random
# import my_module
# random_integer = random.randint(1,10)
# print(random_integer)
#
# print(my_module.my_favourite_number)
# random_number_0_to_1 =random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)
# random_integer = random.randint(1,2)
# print(random_integer)
# if random_integer==1:
#     print("Head")
# else:
#     print('Trails')
#List datastructure

# fruits = ["Apple","Orange","banana"]
# random.choices(fruits)
# fruits[1]="Guava"
# print(fruits)
# fruits.append("Malta")
# print(fruits)
# fruits.extend(["AamRas","Ambarsariya"])
# print(fruits)
# print("Apple")
# print(random.choices(fruits))
# vegetables = ["Spinach","Potatoes"]
# mix = [fruits,vegetables]
# print(mix[1][1])
rock = """"
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissor = """"
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""
print("What do you choose? ")
list =[rock,paper,scissor]
y = int(input("Type O for Rock, 1 for paper or 2 for Scissors.\n"))
x = random.randint(0,2)

print(list[y])
print("Computer chose:")
print(list[x])
print(x)
if(x==0):
    print(rock)
elif(x==1):
    print(paper)
elif(x==2):
    print(scissor)

if(x==0 and y ==0):
    print("Draw")
elif(x==1 and y==1):
    print("Draw")
elif(x==2 and y==2):
    print("Draw")
elif(x==0 and y==1):
    print("You Won")
elif(x==0 and y==2):
    print("Ypu lose")
elif(x==1 and y==1):
    print("Draw")
# elif(x==1 and y==2)



