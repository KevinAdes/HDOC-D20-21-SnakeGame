from turtle import Turtle
import random


class Snake:
    snake_head = Turtle("square")
    snake_head.penup()
    snake_head.color("white")
    snake_head.speed(1)
    snake_segments = [snake_head]

    def add_segment(self):
        final_index = len(self.snake_segments) - 1
        last_segment = self.snake_segments[final_index]
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.speed(1)
        offset = 0
        if last_segment.heading() == 0:
            offset = (-20, 0)
        elif last_segment.heading() == 90:
            offset = (0, -20)
        elif last_segment.heading() == 180:
            offset = (20, 0)
        elif last_segment.heading() == 270:
            offset = (0, 20)
        new_segment.setposition(last_segment.pos()[0] + offset[0], last_segment.pos()[1] + offset[1])
        new_segment.setheading(self.snake_segments[final_index].heading())
        self.snake_segments.append(new_segment)

    def init(self):
        self.add_segment()
        self.add_segment()

    def update_snake_location(self):
        self.snake_head.forward(20)
        cached_heading = self.snake_head.heading()
        for _ in range(1, len(self.snake_segments)):
            self.snake_segments[_].forward(20)
            segment_heading = self.snake_segments[_].heading()
            self.snake_segments[_].setheading(cached_heading)
            cached_heading = segment_heading

    def kill_check(self):
        if (self.snake_head.pos()[0] < -300 or self.snake_head.pos()[0] > 300
                or self.snake_head.pos()[1] < -300 or self.snake_head.pos()[1] > 300):
            return True
        for _ in range(1, len(self.snake_segments)):
            segment_position = self.snake_segments[_].pos()
            dist_to_segment = self.snake_head.distance(segment_position[0], segment_position[1])
            if dist_to_segment <= 10:
                return True
        return False

    def food_check(self, food_position=(int, int)):
        dist_to_food = self.snake_head.distance(food_position[0], food_position[1])
        if dist_to_food <= 10:
            return True
        else:
            return False

    def move_up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def move_right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def move_left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def move_down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)