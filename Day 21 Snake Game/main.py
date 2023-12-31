from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard 


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Collision with food 
    if snake.segments[0].distance(food) <15:
        food.create_food()
        scoreboard.increase_score()
        snake.increase_snake_size()

    # Collison with wall 
    if snake.segments[0].xcor() > 280 or snake.segments[0].ycor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() < -280:
        game_is_on = False 
        scoreboard.game_over()

    # Collision with tail. 

    for seg in snake.segments[1:] :
        if snake.segments[0].distance(seg) < 5:
            game_is_on = False 
            scoreboard.game_over()



screen.exitonclick()