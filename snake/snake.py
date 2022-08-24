import Turtle

class Snake(Turtle):
  def __init__(self, shape, color, speed):
    Turtle.__init__(self, shape)
    self.color(color)
    self.speed(speed)
    x_cor = self.xcor()
    y_cor = self.ycor()

    def move_snake(self):
        for seg_num in range(len(snake_body) - 1, 0, -1):
          new_x = snake_body[seg_num - 1].xcor()
          new_y = snake_body[seg_num - 1].ycor()
          snake_body[seg_num].goto(new_x, new_y)
          snake_body[0].forward(20)

