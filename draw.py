from turtle import Turtle


class Draw(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-270, -270)
        self.pendown()
        self.color('white')
        for _ in range(4):
            self.fd(540)
            self.left(90)
