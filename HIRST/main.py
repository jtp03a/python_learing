"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
import random
import colorgram

t = turtle.Turtle()
s = turtle.Screen()


turtle.colormode(255)


# t.width(1)
t.speed("fastest")

def get_hirst_colors(file_name, num_colors):
  colors = colorgram.extract(file_name, num_colors)
  
  hirst_colors = []
  
  for color in colors:
    rgb = color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    hirst_colors.append((r, g, b))

  return hirst_colors

# file_name = input("Input file name of Hirst style to emulate: ")
# num_colors = int(input("Input number of colors to extract: "))

file_name = "python_hirst.jpg"
num_colors = 100

color_list = get_hirst_colors(file_name, num_colors)
print(color_list)

screen_size = 1000
dot_size = int((screen_size * 0.05))
num_dots = 10

screen_segments = int(screen_size / num_dots)

print(screen_segments)

s.setup(screen_size, screen_size)

t.hideturtle()
t.penup()

y_pos = int(((screen_size / 2 ) - screen_size) + dot_size)
x_pos = int(((screen_size / 2 ) - screen_size) + dot_size)

print(y_pos)
print(x_pos)

t.goto(x_pos,y_pos)

for _ in range(num_dots):
  for _ in range(num_dots):
    t.dot(dot_size, random.choice(color_list))
    t.forward(screen_segments)
  y_pos += screen_segments
  t.goto(x_pos, y_pos)

s.exitonclick()

# def random_rgb_color():
#   r = random.randint(0, 255)
#   g = random.randint(0, 255)
#   b = random.randint(0, 255)
#   rand_color = (r, g, b)
#   return rand_color

# def set_line(cir_degrees):
#   t.setheading(cir_degrees)
#   t.color(random_rgb_color())
  
# for cir_degrees in range(0, 360, 10):
#   set_line(cir_degrees)
#   t.circle(100)