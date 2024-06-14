from turtle import Turtle, Screen
import time
import random

screen = Screen()
screen.tracer(0, 1)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_length = 3

snake_head = Turtle("square")
snake_head.penup()
snake_head.color("white")
snake_head.speed(1)

food = Turtle("turtle")
food.penup()
food.color("green")


snake_segments = [snake_head]


def add_segment():
    final_index = len(snake_segments) - 1
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.speed(1)
    new_segment.setposition(snake_segments[final_index].pos()[0], snake_segments[final_index].pos()[1])
    new_segment.setheading(snake_segments[final_index].heading())
    snake_segments.append(new_segment)


def initialize_snake():
    add_segment()
    add_segment()
    snake_segments[1].setposition(-20, 0)
    snake_segments[2].setposition(-40, 0)


def update_food_location():
    food_xcor = 20 * random.randint(-10, 10)
    food_ycor = 20 * random.randint(-10, 10)
    print(food_xcor)
    print(food_ycor)
    food.setposition(food_xcor, food_ycor)


def update_snake_location():
    snake_head.forward(20)
    if snake_head.pos() == food.pos():
        update_food_location()
        add_segment()
    cached_heading = snake_head.heading()
    for _ in range(1, len(snake_segments)):
        snake_segments[_].forward(20)
        segment_heading = snake_segments[_].heading()
        snake_segments[_].setheading(cached_heading)
        cached_heading = segment_heading
    time.sleep(.1)
    screen.update()


def kill_check():
    global run_game
    if (snake_head.pos()[0] < -300 or snake_head.pos()[0] > 300
            or snake_head.pos()[1] < -300 or snake_head.pos()[1] > 300):
        return True
    for _ in range(1, len(snake_segments)):
        if snake_head.pos() == snake_segments[_].pos():
            run_game = False
            screen.bye()
            return True
    return False


def move_up():
    if snake_head.heading() != 270:
        snake_head.setheading(90)


def move_right():
    if snake_head.heading() != 180:
        snake_head.setheading(0)


def move_left():
    if snake_head.heading() != 0:
        snake_head.setheading(180)


def move_down():
    if snake_head.heading() != 90:
        snake_head.setheading(270)


screen.listen()
screen.onkey(key="w", fun=move_up)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="s", fun=move_down)


initialize_snake()
update_food_location()

run_game = True
while run_game:
    update_snake_location()
    if kill_check():
        screen.bye()
        run_game = False

