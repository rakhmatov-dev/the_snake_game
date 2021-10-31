from turtle import Turtle
from collections import namedtuple

POINT = namedtuple("Point", "x y")
INITIAL_COR = POINT(0, 0)
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        for n in range(3):
            self.add_segment((INITIAL_COR.x - 20 * n, INITIAL_COR.y))
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto((self.segments[index - 1].xcor(), self.segments[index - 1].ycor()))
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def extend(self):
        # add new segment to the snake
        self.add_segment(self.segments[-1].position())
