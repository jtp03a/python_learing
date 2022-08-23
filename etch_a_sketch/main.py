from turtle import Turtle, Screen

t = Turtle()
s = Screen()

def move_forwards():
  t.forward(10)

def turn_right():
  t.right(10)

def move_back():
  t.backward(10)

def turn_left():
  t.left(10)

def screen_clear():
  t.clear()
  t.penup()
  t.hideturtle()
  t.home()
  t.showturtle()
  t.pendown()

s.listen()
s.onkey(key="d", fun=move_forwards)
s.onkey(key="a", fun=move_back)
s.onkey(key="s", fun=turn_right)
s.onkey(key="w", fun=turn_left)
s.onkey(key="c", fun=screen_clear)
s.exitonclick()