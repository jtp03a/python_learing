from turtle import Screen
import time
from snake import Snake

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

t = Snake()

t.create_snake()



# snake_body = []
# current_snake_length = 3

# x_pos = 0

# for _ in range(current_snake_length):
#   snake_body.append(Snake_Turtle(shape="square", color="white", speed="fastest"))

# for segment in snake_body:
#   segment.penup()
#   segment.goto(x_pos, 0)
#   x_pos -= 20

# s.update()

# snake_is_moving = True

# while snake_is_moving:
#   s.update()
#   time.sleep(0.1)
  



s.exitonclick()