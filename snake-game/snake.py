from turtle import Turtle
from time import sleep

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, no_of_segments):
        self.no_of_segments = no_of_segments
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x_cor = 0
        y_cor = 0
        for i in range(self.no_of_segments):
            self.segments.append(Turtle("square"))
            self.segments[i].color("white")
            self.segments[i].penup()
            self.segments[i].goto((x_cor, y_cor))
            x_cor -= 20

    def create_segment(self):
        self.segments.append(Turtle("square"))
        self.segments[self.no_of_segments].color("white")
        self.segments[self.no_of_segments].penup()
        self.segments[self.no_of_segments].goto(self.segments[self.no_of_segments - 1].pos())
        self.no_of_segments += 1

    def move(self):
        sleep(0.1)
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.head.forward(20)
        # Inorder to make all segments follow head. Copy 3rd to 2nd, 2nd to 1st
        # self.segments[2].goto(self.segments[1].pos())
        # self.segments[1].goto(self.segments[0].pos())
        # self.segments[0].forward(20)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
