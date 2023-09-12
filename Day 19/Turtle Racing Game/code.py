from turtle import Turtle, Screen 
import random


screen = Screen()
u_input = screen.textinput(title="Make your Bet ", prompt='Which Turtle will win?Enter a color:')
screen.setup(width=500,height=400)

yPositions = [0,30,60,90,-30,-60,-90]
colors = ['red','blue','green','cyan','orange','purple','pink']
random.shuffle(colors)

turtles = []

#creating Turtle object
for i in range(7):
    tim = Turtle(shape='turtle')
    turtles.append(tim)
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230,y=yPositions[i])


race_is_on = False

if u_input:
    race_is_on = True 


while race_is_on == True:
    for t in turtles:
        if t.xcor() > 230:
            race_is_on = False 
            break


        speed = random.randint(1,10)
        t.forward(speed)

dic ={}
distance =[]
for turtle in turtles:
    dic[turtle.xcor()] = turtle.pencolor()
    distance.append(turtle.xcor())



distance.sort(reverse=True)

if u_input == dic[distance[0]]:
    print(f"Yes You win!\n{dic[distance[0]]} turtle is the winner!!")
else:
    print(f"You lost\n{dic[distance[0]]} turtle is the winner!!")


print("\nRace Details:")
for i in range(7):
    print(f"{dic[distance[i]]} turtle obtainded position: {i+1}" )


















screen.exitonclick()