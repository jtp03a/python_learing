from turtle import Screen, Turtle
import time
from car import Car
from level import Level
import random

s = Screen()
s.setup(width=600, height=600)
s.title("Turtle Crossing")
s.tracer(0)

turtle = Turtle()
turtle.penup()
turtle.shape("turtle")
turtle.setheading(90)
turtle.goto(0, -280)

car_manager = Car()
level = Level()

def turtle_up():
  turtle.forward(20)

s.listen()
s.onkeypress(turtle_up, "w")

running = True

while running:
  s.update()
  time.sleep(0.1)

  car_manager.create_car()
  car_manager.move()

  #Detect collision with car
  for car in car_manager.cars:
    if turtle.distance(car) < 20:
      running = False
      level.game_over()

  #Detect reaching the level end
  if turtle.ycor() > 280:
    turtle.goto(0, -280)
    car_manager.inc_move()
    level.inc_level()

s.exitonclick()