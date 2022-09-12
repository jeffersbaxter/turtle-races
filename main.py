from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
all_turtles = []


def create_turtle(color, y_axis):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.pu()
    new_turtle.goto(x=-240, y=y_axis)
    all_turtles.append(new_turtle)
    return new_turtle


create_turtle("red", 150)
create_turtle("orange", 100)
create_turtle("gold", 50)
create_turtle("green", 0)
create_turtle("blue", -50)
create_turtle("indigo", -100)
create_turtle("violet", -150)

if user_bet:
    is_race_on = True

while is_race_on:
    for current_turtle in all_turtles:
        move = random.randint(1, 10)
        current_turtle.forward(move)
        if current_turtle.xcor() > 230:
            is_race_on = False
            winning_color = current_turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle crossed first!")
            else:
                print(f"You lose! The {winning_color} turtle crossed first!")

screen.exitonclick()
