# import another_module
# import turtle
#
# print(another_module.another_var)
#
# timmy = turtle.Turtle()
# print(timmy)
#
# timmy.shape("turtle")
#
#
# timmy.color("coral")
# timmy.forward(250)
#
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable
table = prettytable.PrettyTable()

table.add_column('Pokemon_Name', ["pikach", "Squirtle", "Charmander"])
table.add_column('Type', ["Electric", "Water", "Fire"])

table.align = "r"
print(table)