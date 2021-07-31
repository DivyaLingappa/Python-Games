from time import sleep
from turtle import Turtle, Screen
import random
from snake import Snake
from food import Food
from score import ScoreBoard

s = Screen()
s.setup(width=600, height=600)
s.title('Snake game')
s.bgcolor("black")
s.tracer(0)


def main():
    game_on = True
    snake = Snake(3)
    food = Food()
    score = ScoreBoard()
    s.listen()
    s.onkey(key="Up", fun=snake.move_up)
    s.onkey(key="Down", fun=snake.move_down)
    s.onkey(key="Right", fun=snake.move_right)
    s.onkey(key="Left", fun=snake.move_left)
    while game_on:
        s.update()
        snake.move()
        if snake.head.distance(food) < 15:
            snake.create_segment()
            food.goto(random.randint(-280, 280), random.randint(-280, 280))
            score.update_score()
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            score.game_over()
            game_on = False
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.game_over()
                game_on = False


if __name__ == '__main__':
    main()

s.exitonclick()
