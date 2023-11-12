import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    #Detect Collision with car 
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False 
            scoreboard.show_game_over()
            


    #Finishing Line touches 
    if player.ycor() > 280 :
        player.goto(0,-280)
        car_manager.increase_car_speed()
        scoreboard.level_up()

    




screen.exitonclick()
