from turtle import Turtle

class ScoreBoard(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.color("white")
    self.penup()
    self.setpos(0, 280)
    self.current_score = 0
    self.high_score = 0
    self.get_high_score()
    self.write_score()


  def write_score(self):
    self.clear()
    self.write(f"Score: {self.current_score} | High Score: {self.high_score}", align="center", font=("Ariel", 12, "normal"))

  def inc_score(self):
    self.current_score += 1
    self.write_score()

  def reset(self):
    if self.current_score > self.high_score:
      self.high_score = self.current_score
      with open("data.txt", "w") as data:
        data.write(str(self.current_score))
    self.current_score = 0
    self.write_score()

  def get_high_score(self):
    with open("data.txt", "r") as data:
      self.high_score = int(data.read())

  # def game_over(self):
  #   self.home()
  #   self.write("Game Over", align="center", font=("Ariel", 16, "normal"))