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
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} - High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.teleport(0, 0)
    #     self.color("red")
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
