from turtle import Turtle
import random


class Food:
    food_obj = Turtle("turtle")
    food_obj.penup()
    food_obj.color("green")

    def update_food_location(self):
        food_xcor = 20 * random.randint(-10, 10)
        food_ycor = 20 * random.randint(-10, 10)
        print(food_xcor)
        print(food_ycor)
        self.food_obj.setposition(food_xcor, food_ycor)

    def get_food_position(self):
        return self.food_obj.pos()