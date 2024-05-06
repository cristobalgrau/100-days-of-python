from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.teleport(-250, 250)
        self.level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)
