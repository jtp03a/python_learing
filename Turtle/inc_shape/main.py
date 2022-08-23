import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.screensize(700, 700)

shape_sides = 5
angle = 360 / shape_sides

for _ in range(25):
  for _ in range(shape_sides):
    t.forward(100)
    t.right(angle)
  shape_sides += 1  
  angle = 360 / shape_sides