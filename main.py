# TODO Part 1. Create a snake body | DONE
# TODO Part 2. Move the snake
# TODO Part 3. Control the snake
# TODO Part 4. Detect collisions with food
# TODO Part 5. Create a scoreboard
# TODO Part 6. Detect collision with wall
# TODO Part 7. Detect collision with tail

from turtle import Turtle, Screen
import time

x_left, y_left, x_right, y_right = [None, None, None, None]


def initialize_snake(snake_length, x_cor, y_cor):
    snake = []
    for n in range(snake_length):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto((x_cor - 20 * n, y_cor))
        snake.append(new_segment)
    return snake


def move_the_snake(snake):
    global x_left, y_left, x_right, y_right
    for index in range(len(snake)):
        snake[index].forward(10)
        if index != 0:
            if (snake[index].xcor() == x_left
                    and snake[index].ycor() == y_left):
                snake[index].left(90)
                if index == len(snake) - 1:
                    x_left, y_left = [None, None]
            elif (snake[index].xcor() == x_right
                    and snake[index].ycor() == y_right):
                snake[index].right(90)
                if index == len(snake) - 1:
                    x_right, y_right = [None, None]


def go_left():
    global x_left, y_left
    snake[0].left(90)
    x_left = snake[0].xcor()
    y_left = snake[0].ycor()


def go_right():
    global x_right, y_right
    snake[0].right(90)
    x_right = snake[0].xcor()
    y_right = snake[0].ycor()


def append_segment():
    pass


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(key="d", fun=go_right)
screen.onkey(key="a", fun=go_left)

snake = initialize_snake(snake_length=3, x_cor=0, y_cor=0)
screen.update()

game_is_on = True
while game_is_on:
    move_the_snake(snake)
    screen.update()
    time.sleep(1)

screen.exitonclick()
