from turtle import Turtle 

XPOSITIONS = [0,-20,-40]
MOVE_DISTANCE = 10
UP = 90 
DOWN = 270 
LEFT = 180 
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        
    def create_snake(self): 
        for i in range(3):
            tim = Turtle(shape='square')
            tim.color("white")
            tim.penup()
            tim.goto(x =XPOSITIONS[i],y=0)
            self.segments.append(tim) 

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)
    
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)
    
    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)
    
    def right(self):
        if self.segments[0].heading()!=LEFT:
            self.segments[0].setheading(0)

