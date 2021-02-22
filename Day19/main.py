from turtle import Turtle, Screen
import random

# # Etch-A-Sketch
# def move_forward():
#     tim.forward(10)
#
#
# def move_backward():
#     tim.backward(10)
#
#
# def move_counterclock():
#     tim.left(10)
#
#
# def move_clockwise():
#     tim.right(10)
#
#
# def clear_screen():
#     tim.clear()
#     tim.reset()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_clockwise)
# screen.onkey(key="d", fun=move_counterclock)
# screen.onkey(key="c", fun=clear_screen)


# Turtle Racing Game

is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make you Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for our_turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        our_turtle.forward(rand_distance)
        if our_turtle.xcor() > 230:
            is_race_on = False
            win_color = our_turtle.pencolor()
            if win_color == user_bet:
                print("You've won! The color of the winning turtle is {}".format(win_color))
            else:
                print("You've Lost! The color of the winning turtle is {}".format(win_color))
            break

screen.exitonclick()
