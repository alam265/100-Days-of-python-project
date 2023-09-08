import random 

print("Welcome To the Guessing Number Game!!")
print("Lets guess a number 1 to 100")

difficulty = input("Enter Difficulty level: type 'Easy' or 'Hard'").lower()

generated_number = random.randint(1,100)

attempt = 0 

if difficulty == "easy":
    attempt = 10 
    print("You have total 10 attempts")
else:
    attempt = 5 
    print("You have total 5 attempts")


while attempt !=0:
    guessed_number = int(input("Guess Number: "))
    if guessed_number == generated_number:
        print("Yes, guess was right. Number was",generated_number)
        break 
    elif guessed_number > generated_number:
        print("Too High")
    else:
        print("Too low")
    attempt-=1 
    if attempt!=0:
        print(f"Gauess again.\nYou have {attempt} attempts left")
if attempt == 0:
    print("You've run out of guesses. You loose")

