import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_tims = []

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    tim.speed("fastest")
    all_tims.append(tim)



if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_tims:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!")

        move_forward = random.randint(0, 10)
        turtle.forward(move_forward)

screen.exitonclick()