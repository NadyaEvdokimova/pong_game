from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from middle_net import MiddleNet
import time

screen = Screen()
screen.bgcolor("black")
screen.title("My Pong game")
screen.setup(width=800, height=600)
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
middle_net = MiddleNet()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if the ball goes out of bounds
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()




























screen.exitonclick()
