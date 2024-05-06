from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        # The turtle starts on 20px by 20px size, so we have to stretch 5 time the width and the len stays in 1 (20px)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), y=new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), y=new_y)
