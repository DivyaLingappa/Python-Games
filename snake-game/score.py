from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.no_of_score = 0
        self.color("white")
        self.penup()
        self.goto(240, 270)
        self.hideturtle()
        self.write(f'Score: {self.no_of_score}', align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.no_of_score += 1
        self.clear()
        self.write(f'Score: {self.no_of_score}', align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align="center", font=("Arial", 30, "normal"))
