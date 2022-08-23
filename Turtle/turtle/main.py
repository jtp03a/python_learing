# from turtle import Turtle, Screen

import turtle as t
import heroes

timmy = t.Turtle()

# print(timmy)

timmy.shape("turtle")
timmy.color('coral')
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)

mov_range = 10

for _ in range(5):
  for _ in range(4):
    for _ in range(4):
      timmy.forward(mov_range)
      timmy.pu()
      timmy.forward(mov_range)
      timmy.pd()
    timmy.left(90)
  mov_range += 5


  # timmy.left(90)

my_screen = t.Screen()

# print(my_screen.canvheight)

my_screen.exitonclick()

print(heroes.gen())

# from prettytable import PrettyTable

# table = PrettyTable()

# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])

# table.align = "l"

# print(table)