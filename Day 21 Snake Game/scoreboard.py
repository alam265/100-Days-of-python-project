from turtle import Turtle 

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(x=0,y=270)
        self.write(f"Score: {self.score}",align='center', font=('Coueier', 20, 'bold'))
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align='center', font=('Courier', 20, 'bold'))
      
    def increase_score(self):
        self.clear()
        self.score+=1 
        self.write(f"Score: {self.score}",align='center', font=('Courier', 20, 'bold'))


