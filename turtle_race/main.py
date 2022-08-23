from turtle import Turtle, Screen, fillcolor
import random

class Race_Turtle(Turtle):
  def __init__(self, shape, color):
    Turtle.__init__(self, shape)
    self.color(color)

s = Screen()

s.setup(width=500, height=400)

bet = s.textinput(title="Place your bet", prompt="Enter a color")

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

print(bet)

turtles = []

for color in colors:
  turtles.append(Race_Turtle(shape="turtle", color=color))

y_pos = -100

for turtle in turtles:
  turtle.penup()
  turtle.goto(-230, y_pos)
  y_pos += 50

is_race_on = False

if bet:
  is_race_on = True

while is_race_on:
  for turtle in turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == bet:
        print(f"You won, The {winning_color} turtle is the winner")
      else:
        print(f"You lost, The {winning_color} turtle is the winner")
    movement = random.randint(0, 10)
    turtle.forward(movement)


s.exitonclick()