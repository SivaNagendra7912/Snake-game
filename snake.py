from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_list = []
        self.initial_cords = [0, -20, -40]

    def creates_snakes(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.snake_list.append(snake)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[i - 1].xcor()
            new_y = self.snake_list[i - 1].ycor()
            self.snake_list[i].goto(new_x, new_y)
        self.snake_list[0].fd(20)

    def up(self):
        if self.snake_list[0].heading() != 270:
            self.snake_list[0].setheading(90)

    def down(self):
        if self.snake_list[0].heading() != 90:
            self.snake_list[0].setheading(270)

    def left(self):
        if self.snake_list[0].heading() != 0:
            self.snake_list[0].setheading(180)

    def right(self):
        if self.snake_list[0].heading() != 180:
            self.snake_list[0].setheading(0)
