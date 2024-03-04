from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 265)
        self.write(f"Score: {self.score}", align='center', font=('courier', 24, 'normal'))
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=('courier', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('courier', 24, 'normal'))
        self.goto(0, -35)
        self.write(f"Your Score is {self.score}",align='center', font=('courier', 22, 'normal'))
