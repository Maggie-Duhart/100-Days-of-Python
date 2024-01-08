import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)

# text input - Pop up window
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
all_speed = ["fastest", "fast", "normal", "slow", "slowest"]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        rand_speed = random.choice(all_speed)
        turtle.speed(rand_speed)
        turtle.forward(rand_distance)



screen.exitonclick()


# Make an Etch-A-Sketch App Project Below

# tim = Turtle()
# screen = Screen()

# # turtle will move forward 10
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def move_counter_clockwise():
#     tim.left(45)
#
#
# def move_clockwise():
#     tim.right(45)
#
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# # # onkey is an event listener - fun = functions with no arguments, and the key from keyboard
# # # when the SPACE KEY IS PRESS, we move forwards. The fun here goes without () bc will only happens if the key is press
# # screen.onkey(key="space", fun=move_forwards)
#
# # start listening events
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_counter_clockwise)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="c", fun=clear_screen)

# screen.exitonclick()
