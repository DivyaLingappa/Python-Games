from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.turtlesize(0.5)
        self.penup()
        self.x_mov = 10
        self.y_mov = 10
        self.move_speed = 0.1

    def move(self):
        x_new = self.xcor() + self.x_mov
        y_new = self.ycor() + self.y_mov
        self.goto(x_new, y_new)

    def bounce_y(self):
        self.y_mov *= -1

    def bounce_x(self):
        self.x_mov *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.x_mov *= -1
        self.move_speed = 0.1
