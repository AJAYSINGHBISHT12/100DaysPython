import random
random_value = random.randint(1,100)
def after_check(cnt):
    while cnt>0:
        y = int(input(f"you have {cnt} attempts remaining to guess the number.\nmake a guess:"))
        if y > random_value:
            print("Too high.\nGuess again.")
            cnt = cnt - 1
        elif y == random_value:
            print(f"You got it! The answer was {random_value}")
        if y < random_value:
            print("Too low.\nGuess again.")
            cnt = cnt - 1

def final():
    if x == "easy":
        after_check(10)
    elif x == "hard":
        after_check(5)
print(f"Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
x=str(input("Choose a difficulty. Type 'easy' or 'hard':")).lower()
final()
