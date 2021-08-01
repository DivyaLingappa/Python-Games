from turtle import Turtle


class Partition(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pensize(5)
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
