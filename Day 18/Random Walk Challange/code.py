from turtle import Turtle , Screen
import random 

t = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [90,180,270,0]

t.pensize(15)
t.speed('fastest')

for _ in range(200):
    t.color(random.choice(colours))
    t.forward(30)
    t.setheading(random.choice(directions))













screen = Screen()
screen.exitonclick()
