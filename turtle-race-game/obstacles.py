from turtle import Turtle
import random

MOVE_LEFT = 180
OBSTACLE_XCOR = 500

color_list = ['red', 'green', 'black', 'orange', 'yellow', 'cyan', 'skyblue', 'purple', 'magenta', 'chocolate', 'brown',
              'gold', 'maroon', 'turquoise', 'violet']


class Obstacles(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(random.choice(color_list))
        self.penup()
        self.goto(OBSTACLE_XCOR, random.randint(-320, 320))
        self.setheading(MOVE_LEFT)
