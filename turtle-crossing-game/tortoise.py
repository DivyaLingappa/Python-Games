from turtle import Turtle

TORTOISE_SIZE = 2
MOVE_UP = 90
TORTOISE_POSITION = (0, -370)
GAME_OVER_POSITION = (-130, 0)


class Tortoise(Turtle):
    def __init__(self):
        super().__init__()
        self.tortoise_speed = 10
        self.shape("turtle")
        self.shapesize(TORTOISE_SIZE)
        self.color("darkgreen")
        self.penup()
        self.setheading(MOVE_UP)
        self.goto(TORTOISE_POSITION)

    def move_up(self):
        self.forward(self.tortoise_speed)

    def reset(self):
        self.goto(TORTOISE_POSITION)
        self.tortoise_speed += 5

    def game_over(self):
        self.color("black")
        self.goto(GAME_OVER_POSITION)
        self.write('GAME OVER', font=('Ariel', 50, 'normal'))
