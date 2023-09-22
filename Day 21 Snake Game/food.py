from turtle import Turtle 
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.create_food()

    def create_food(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.penup()
        self.goto(random_x,random_y)


