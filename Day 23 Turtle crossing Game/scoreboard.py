from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0 
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-220,250) 
        self.write(f"Level: {self.level}",align='center',font=FONT)


    def level_up(self):
        self.level+=1 
        self.clear()
        self.write(f"Level: {self.level}",align='center',font=FONT)


    def show_game_over(self):
        self.penup()
        self.goto(0,0)
        self.write(f"Game Over",align='center',font=FONT)
      
