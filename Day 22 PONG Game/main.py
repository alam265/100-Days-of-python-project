from turtle import Screen , Turtle 
from paddle import Paddle
from ball import Ball 
from scoreboard import ScoreBoard
import time


screen = Screen() 
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))


ball = Ball()
score = ScoreBoard()







screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")

game_is_on = True 

while game_is_on:

    time.sleep(ball.move_speed)
    
    screen.update()
    ball.move()
    
    # Ball colide with upper and lower screen
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Ball colide with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #Right paddle miss the ball 
    if ball.xcor() > 370:
        ball.reset_position()
        score.l_point()

    #Left paddle miss the ball 
    if ball.xcor() <-370:
        ball.reset_position()
        score.r_point()

screen.exitonclick()