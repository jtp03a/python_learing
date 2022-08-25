from turtle import Turtle

class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.color("white")
    self.penup()
    self.setpos(0, 280)
    self.current_score = 0
    self.write_score()

  def write_score(self):
    self.clear()
    self.write(f"Score: {self.current_score}", align="center", font=("Ariel", 12, "normal"))

  def inc_score(self):
    self.current_score += 1
    self.write_score()

  def game_over(self):
    self.home()
    self.write("Game Over", align="center", font=("Ariel", 16, "normal"))