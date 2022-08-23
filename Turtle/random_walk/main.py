import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()

s.screensize(500, 500)

directions = [0, 90, 180, 270]
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
num_walks = random.randint(1, 100)
t.width(10)

def set_line():
  t.setheading(random.choice(directions))
  t.color(random.choice(colors))
  
for _ in range(num_walks):
  set_line()
  t.forward(30)