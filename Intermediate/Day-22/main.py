from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("wall")

    # Detect collision with r_paddle
    if (ball.distance(r_paddle) < 50 and 330 < ball.xcor() < 350) or (ball.distance(l_paddle) < 50 and -330 > ball.xcor() > -350):
        ball.bounce("paddle")

    # Detect r_paddle miss the ball
    if ball.xcor() > 400:
        ball.reset_ball()
        score.l_point()

    # Detect l_paddle miss the ball
    if ball.xcor() < -400:
        ball.reset_ball()
        score.r_point()

screen.exitonclick()
