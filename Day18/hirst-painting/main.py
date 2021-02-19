
import turtle
import random
turtle.colormode(255)

# # Getting Colors from existing image
# import colorgram
# colors = colorgram.extract("painting_orginal.jpg", 30)
# color_pallet = []
# for i in range(len(colors)):
#     # print(colors[i].rgb)
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     color_pallet.append((r, g, b))
# print(color_pallet)

color_pallet = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),
                (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252),
                (243, 33, 165), (229, 17, 121), (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61),
                (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239), (81, 73, 214), (238, 156, 220),
                (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
tim = turtle.Turtle()


tim.penup()
for y in range(0, 10):
    for x in range(0, 10):
        tim.setx(x*50)
        tim.sety(y*50)
        tim.dot(20, random.choice(color_pallet))

screen = turtle.Screen()
screen.exitonclick()
