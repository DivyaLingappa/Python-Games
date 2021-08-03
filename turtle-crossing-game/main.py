from turtle import Turtle, Screen
from time import sleep
import random
from tortoise import Tortoise
from obstacles import Obstacles
from levels import DifficultyLevels

screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("white")
screen.title("TURTLE CROSSING GAME")
screen.tracer(0)


def main():
    game_on = True
    obstacles_list = []
    obstacles_speed = 10
    tortoise = Tortoise()
    levels = DifficultyLevels()
    screen.listen()
    screen.onkey(key="Up", fun=tortoise.move_up)

    while game_on:
        sleep(0.1)
        screen.update()
        #  Inorder to generate obstacles randomly, use chance
        # So,an obstacle is generated everytime 1 is picked randomly
        # It's like throwing a dice
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            obstacles_list.append(Obstacles())
        for obstacle in obstacles_list:
            obstacle.forward(obstacles_speed)
        for obstacle in obstacles_list:
            if tortoise.distance(obstacle) < 30:
                tortoise.game_over()
                game_on = False
        if tortoise.ycor() > 380:
            tortoise.reset()
            levels.increase_difficulty()
            obstacles_speed += 5


if __name__ == '__main__':
    main()

screen.exitonclick()
