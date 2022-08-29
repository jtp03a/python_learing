from turtle import Turtle

class Level(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.color("black")
    self.penup()
    self.setpos(-280, 280)
    self.current_level = 1
    self.write_score()

  def write_score(self):
    self.clear()
    self.write(f"Level: {self.current_level}", align="left", font=("Ariel", 12, "normal"))

  def inc_level(self):
    self.current_level += 1
    self.write_score()

  def game_over(self):
    self.home()
    self.write("Game Over", align="center", font=("Ariel", 16, "normal"))