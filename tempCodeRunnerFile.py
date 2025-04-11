from turtle import Screen
from paddle_module import Paddle
from ball import Ball
import time

# Setup screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create paddles and ball
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

# Control bindings
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.08)
    screen.update()
    ball.move()

    #Detect collison with wall 
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce_y
          ball.bounce_y()
    
    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
        

screen.exitonclick()
