import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()

s.screensize(500, 500)
turtle.colormode(255)

directions = [0, 90, 180, 270]
t.width(10)
num_walks = 200   

def random_rgb_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  rand_color = (r, g, b)
  return rand_color

def set_line():
  t.setheading(random.choice(directions))
  t.color(random_rgb_color())
  
for _ in range(num_walks):
  set_line()
  t.forward(30)