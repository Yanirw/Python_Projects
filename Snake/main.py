from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from motivationals import Motivationals
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Super Cool Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
motivation = Motivationals()


screen.onkey(snake.up, "Up") 
screen.onkey(snake.down,"Down") 
screen.onkey(snake.left,"Left") 
screen.onkey(snake.right,"Right") 

screen.listen()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    # detect collision with food
    if snake.head.distance(food) < 15: 
        food.refresh()
        snake.extent()
        score_board.update_score()
        motivation.new_awsome_text()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        score_board.reset()
        snake.reset()
        game_is_on = False
        score_board.game_over()
    

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
          score_board.reset()
          snake.reset()
          game_is_on = False
           



screen.exitonclick()