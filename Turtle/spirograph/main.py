import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()

s.screensize(1000, 1000)
turtle.colormode(255)


t.width(1)
t.speed("fastest")

def random_rgb_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  rand_color = (r, g, b)
  return rand_color

def set_line(cir_degrees):
  t.setheading(cir_degrees)
  t.color(random_rgb_color())
  
for cir_degrees in range(0, 360, 10):
  set_line(cir_degrees)
  t.circle(100)