from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

RIGHT_PADDLE_POS = (350, 0)
LEFT_PADDLE_POS = (-350, 0)
BALL_POS = (0, 300)

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong")
# s.tracer(0)

r_paddle = Paddle(RIGHT_PADDLE_POS)
l_paddle = Paddle(LEFT_PADDLE_POS)
ball = Ball()
scoreboard = ScoreBoard()

def lpaddle_up():
    global lspeed_y
    lspeed_y = 20

def lpaddle_down():
    global lspeed_y
    lspeed_y = -20

def rpaddle_up():
    global rspeed_y
    rspeed_y = 20

def rpaddle_down():
    global rspeed_y
    rspeed_y = -20

def l_key_release():
    global lspeed_y

    lspeed_y = 0

def r_key_release():
    global rspeed_y

    rspeed_y = 0

# default values at start
lspeed_y = 0
rspeed_y = 0

def update_frame():
    
      l_paddle.move(lspeed_y)

      r_paddle.move(rspeed_y)
      
      ball.move()

      #Detect collision with top or bottom wall
      if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

      # Detect collision with right paddle
      if ball.distance(r_paddle) < 60 and ball.xcor() > 320:
        ball.bounce_x()
        ball.x_move *= 1.2
        ball.y_move *= 1.2

      # Detect collision with left paddle
      if ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        ball.x_move *= 1.2
        ball.y_move *= 1.2

      # Detect out of bounds

      if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()
        
      if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()

      # run again after 50ms
      s.ontimer(update_frame, 50)  # 50ms means ~20 FPS (Frames Per Second) (1000/50 = 20)

s.ontimer(update_frame, 50)

s.listen()
# Left Paddle
s.onkeypress(lpaddle_up, "w")
s.onkeyrelease(l_key_release, "w")
s.onkeypress(lpaddle_down, "s")
s.onkeyrelease(l_key_release, "s")
# Right Paddle
s.onkeypress(rpaddle_up, "Up")
s.onkeyrelease(r_key_release, "Up")
s.onkeypress(rpaddle_down, "Down")
s.onkeyrelease(r_key_release, "Down")

s.mainloop()