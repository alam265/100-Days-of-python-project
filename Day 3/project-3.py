print("          Welcome to Treasure island\nYour Mission is to find the threasue!")

road = input("You're at a cross road. Where you want to go? type 'left' or 'right' ").lower()
if road == 'left':
    lake = input("You come to lake. will you 'swim' or 'wait'?")
    if lake == 'wait':
        door = input("You crossed the lake safely. At this place you found a house. 3 doors. yellow, red, blue. Which one u should pick? ")
         
        if door == 'yellow': 
            print('You win')
        elif door == 'red':
            print("Burned by fire. Game Over")
        elif door == 'blue':
            print("Eaten by beast. Game Over")
        else:
            print("Game Over.")
    else:
        print('You died by crocodile. Game Over')

else:
    print("Fall into a hole. game Over...")






