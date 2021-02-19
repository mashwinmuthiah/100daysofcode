from turtle import Turtle, Screen
import random
import turtle
turtle.colormode(255)
timmy = Turtle()

# # Turtle challenge 1
# for _ in range(0, 4):
#     timmy.forward(100)
#     timmy.right(90)


# # Turtle challenge 2
# for _ in range(0, 15):
#     timmy.pd()
#     timmy.forward(10)
#     timmy.pu()
#     timmy.forward(10)

# Turtle challenge 3

# colors = ["orange red","hot pink","purple","dark slate blue","black"]
# for side in range(3, 11):
#     angle = 360/side
#     timmy.color(random.choice(colors))
#     for _ in range(0, side):
#         timmy.forward(100)
#         timmy.right(angle)

# Turtle challenge 4
timmy.width(width=10)
timmy.speed(100)
for i in range(0, 200):

    timmy.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    timmy.forward(20)
    direction = random.choice(['l', 'r'])
    if direction == 'l':
        timmy.left(90)
    else:
        timmy.right(90)


screen = Screen()
screen.exitonclick()

