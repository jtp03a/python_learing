from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()
    self.shape("square")
    self.penup()
    self.setheading(90)
    self.shapesize(stretch_len=5)
    self.color("white")
    self.goto(position)

  def move(self, speed):
    self.forward(speed)
