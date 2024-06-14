from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
import random

screen = Screen()
screen.tracer(0, 1)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="w", fun=snake.move_up)
screen.onkey(key="d", fun=snake.move_right)
screen.onkey(key="a", fun=snake.move_left)
screen.onkey(key="s", fun=snake.move_down)

snake.init()
food.update_food_location()

run_game = True
while run_game:
    snake.update_snake_location()
    time.sleep(.1)
    screen.update()
    if snake.food_check(food.get_food_position()):
        snake.add_segment()
        food.update_food_location()
        scoreboard.increment_score()
    if snake.kill_check():
        screen.bye()
        run_game = False
