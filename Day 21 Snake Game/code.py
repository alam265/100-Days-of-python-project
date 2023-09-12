from turtle import Turtle, Screen 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")

xPositions = [0,-20,-40]

for i in range(3):
    tim = Turtle(shape='square')
    tim.color("white")
    tim.penup()
    tim.goto(x = xPositions[i],y=0)













screen.exitonclick()