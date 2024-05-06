from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.teleport(y=270)
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.teleport(0, 0)
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
