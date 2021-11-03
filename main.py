from turtle import Screen
import time
from snake import *
from food import Food
from scoreboard import Scoreboard

game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def reset_game():
    scoreboard.reset()
    snake.reset()
    food.refresh()


def close_game():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="space", fun=close_game)

screen.update()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 16:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collisions with wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280
            or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        game_is_on = True
        reset_game()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = True
            reset_game()


screen.exitonclick()
