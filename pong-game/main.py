from turtle import Turtle, Screen
from time import sleep
from paddle import Paddle
from partition import Partition
from ball import Ball
from score import ScoreBoard

s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title("PONG GAME")
s.tracer(0)


def main():
    game_on = True
    paddle_r = Paddle((350, 0))
    paddle_l = Paddle((-350, 0))
    ball = Ball()
    partition = Partition()
    score_l = ScoreBoard((-50, 240))
    score_r = ScoreBoard((20, 240))
    s.listen()
    s.onkey(key="Up", fun=paddle_r.move_up)
    s.onkey(key="Down", fun=paddle_r.move_down)
    s.onkey(key="w", fun=paddle_l.move_up)
    s.onkey(key="s", fun=paddle_l.move_down)
    while game_on:
        s.update()
        sleep(ball.move_speed)
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        if ball.distance(paddle_r) < 50 and ball.xcor() > 340:
            ball.bounce_x()
            score_r.update_score()
        elif ball.distance(paddle_l) < 50 and ball.xcor() < -340:
            ball.bounce_x()
            score_l.update_score()
        elif ball.xcor() > 400:
            score_l.update_score()
            ball.reset()
        elif ball.xcor() < -400:
            score_r.update_score()
            ball.reset()
        if score_r.score == 10 or score_l.score == 10:
            score_r.game_over()
            ball.reset()
            game_on = False


if __name__ == '__main__':
    main()

s.exitonclick()
