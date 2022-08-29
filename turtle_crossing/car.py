from turtle import Turtle
import random

COLORS = ["green", "red", "blue", "yellow", "purple"]
MOVE_SPEED = 5

class Car(Turtle):
  def __init__(self):
    super().__init__()
    self.cars = []
    self.move_speed = 5
    self.hideturtle()
  
  def create_car(self):
    random_car_int = random.randint(1, 6)
    if random_car_int == 1:
      new_car = Turtle("square")
      new_car.penup()
      new_car.shapesize(stretch_len=2)
      new_car.color(random.choice(COLORS))
      rand_y_pos = random.randint(-250, 250)
      new_car.goto(300, rand_y_pos)
      self.cars.append(new_car)

  def move(self):
    for car in self.cars:
      random_speed_mult = random.randint(1,3)
      car.backward(self.move_speed * random_speed_mult)

  def inc_move(self):
    self.move_speed *= 1.3