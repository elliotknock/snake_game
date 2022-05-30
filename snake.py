import turtle
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the first three segments of the snake."""
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """Causes the snake to move and the behind segments to follow the head."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Allows the snake to move up when w is pressed but not backwards on itself."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Allows the snake to move down when s is pressed but not backwards on itself."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Allows the snake to move left when a is pressed but not backwards on itself."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Allows the snake to move right when d is pressed but not backwards on itself."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
