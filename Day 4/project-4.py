dic = {1:'Rock',2:'Paper',3:'Scissors'}

import random 

key = random.randint(1,3)

user = input("Enter your choice:").lower()

print(f"Computer choose: {dic[key]}")


if user == 'rock' :
    if key == 3:
        print(f'\nYou win!!')
    elif key ==2:
        print(f'\nComputer win')
    else:
        print('Match tied')

elif user == 'paper':
    if key == 3:
        print(f"\nComputer win")
    elif key ==1:
        print(f"\nComputer win")
    else:
        print("Match tied")

elif user == 'scissor':
    if key == 1:
        print(f"\nComputer win")
    elif key ==2:
        print(f"\nYou Win !!")
    else:
        print("Match tied")

    
    