from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.turtlesize(0.5)
        self.penup()
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
