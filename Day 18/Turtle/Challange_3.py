from turtle import Turtle, Screen 
import random
t = Turtle()
t.shape("arrow")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

sides = 3 

while sides < 11:
    t.color(random.choice(colours))
    for _ in range(sides):
        t.forward(100)
        t.right(360//sides)
    sides+=1














screen = Screen()
screen.exitonclick()