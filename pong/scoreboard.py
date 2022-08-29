from turtle import Turtle

class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.color("white")
    self.penup()
    self.l_score = 0
    self.r_score = 0
    self.write_score()

  def write_score(self):
    self.clear()
    self.goto(-200, 250)
    self.write(self.l_score, align="center", font=("Ariel", 20, "normal"))
    self.goto(200, 250)
    self.write(self.r_score, align="center", font=("Ariel", 20, "normal"))

  def l_point(self):
    self.l_score += 1
    self.write_score()

  def r_point(self):
    self.r_score += 1
    self.write_score()

  def game_over(self):
    self.home()
    self.write("Game Over", align="center", font=("Ariel", 16, "normal"))