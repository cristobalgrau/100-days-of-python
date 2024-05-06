from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_direction = 10
        self.y_direction = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce(self, hit):
        if hit == "wall":
            self.y_direction *= -1
        elif hit == "paddle":
            self.x_direction *= -1
            self.ball_speed *= 0.9

    def reset_ball(self):
        self.home()
        self.bounce("paddle")
        self.y_direction = random.choice((-10, 10))
        self.ball_speed = 0.1
        self.move()
