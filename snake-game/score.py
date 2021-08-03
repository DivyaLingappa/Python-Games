from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.no_of_score = 0
        self.color("white")
        self.penup()
        self.goto(-170, 265)
        self.hideturtle()
        with open('high_score.txt') as file:
            file_content = file.read()
        self.write(f'Score: {self.no_of_score}      High Score: {file_content}', align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.no_of_score += 1
        self.clear()
        with open('high_score.txt') as file:
            file_content = file.read()
        self.write(f'Score: {self.no_of_score}      High Score: {file_content}' , align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        with open('high_score.txt') as file:
            file_content = file.read()
        if self.no_of_score > int(file_content):
            with open('high_score.txt','w') as file1:
                file1.write(str(self.no_of_score))
        self.goto(0, 0)
        self.write('GAME OVER', align="center", font=("Arial", 30, "normal"))
