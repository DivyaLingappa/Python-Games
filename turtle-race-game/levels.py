from turtle import Turtle

LEVEL_POSITION = (-430, 350)


class DifficultyLevels(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(LEVEL_POSITION)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f'Level: {self.level}', align="center", font=("Arial", 30, "normal"))

    def increase_difficulty(self):
        self.level += 1
        self.update_level()
