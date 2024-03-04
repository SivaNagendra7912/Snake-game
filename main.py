from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from draw import Draw

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

create_snake = Snake()
create_snake.creates_snakes()
screen.listen()
food = Food()
scoreboard_update = ScoreBoard()
border = Draw()

screen.onkey(create_snake.up, "Up")
screen.onkey(create_snake.down, "Down")
screen.onkey(create_snake.left, "Left")
screen.onkey(create_snake.right, "Right")

screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    create_snake.move()
    if create_snake.snake_list[0].distance(food) < 15:
        food.generate_food()
        create_snake.extend()
        scoreboard_update.update_score()
    if create_snake.snake_list[0].xcor() > 260 or create_snake.snake_list[0].xcor() < -260 or create_snake.snake_list[0].ycor() < -265 or create_snake.snake_list[0].ycor() > 265:
        game_is_on = False
        scoreboard_update.game_over()

    for segm in create_snake.snake_list:
        if segm == create_snake.snake_list[0]:
            continue
        elif create_snake.snake_list[0].distance(segm) < 10:
            game_is_on = False
            scoreboard_update.game_over()

screen.exitonclick()
