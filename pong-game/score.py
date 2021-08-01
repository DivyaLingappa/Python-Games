from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.write(f'{self.score}', font=('Ariel', 50, 'normal'))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f'{self.score}', font=('Ariel', 50, 'normal'))

    def game_over(self):
        self.goto(-90, 0)
        self.write('GAME   OVER', font=('Ariel', 30, 'normal'))
