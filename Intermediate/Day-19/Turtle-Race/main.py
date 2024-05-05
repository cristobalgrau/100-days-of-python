from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: \n (red, orange, yellow, "
                                             "green, blue, purple)")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = -100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, y)
    y += 40
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've win!. The {winning_color} turtle is the winner!")
            else:
                print(f"You've loose!. The {winning_color} turtle is the winner!")

        rand_instance = random.randint(0,10)
        turtle.forward(rand_instance)

screen.exitonclick()
