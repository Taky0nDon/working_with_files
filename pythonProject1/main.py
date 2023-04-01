# from turtle import Turtle, Screen
from prettytable import PrettyTable

#
# timmy = Turtle() #timmy is a new Turtle object
# john = Turtle()
# susie = Turtle()
# mark = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("cadetblue1")
# print(timmy.shape())
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

# pikachue, squirtle, charmander
# electric, water, fire
