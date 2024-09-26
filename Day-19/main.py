import turtle
from turtle import Turtle, Screen
import random
from numpy.core.defchararray import title

is_race_on = False
screen = Screen()

# def move_forwards():
#     tim.forward(10)
# def move_backward():
#     tim.backward(10)
# screen.listen()
# screen.onkey(key="F", fun=move_forwards)
# screen.onkey(key="B", fun=move_backward)

screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
x = -230
y = -100
for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x, y)
    y = y + 30
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won! {winning_color} turtle is the winner!")
            else:
                print(f"you lost! {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
screen.exitonclick()