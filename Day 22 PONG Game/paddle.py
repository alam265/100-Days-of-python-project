from turtle import Turtle 
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
    
    def go_up(self):
        new_y = self.ycor()+20
        if new_y < 241:
            self.goto(x=self.position[0], y = new_y)
        

        
    def go_down(self):
        new_y = self.ycor()-20
        self.goto(x=self.position[0], y = new_y)



        