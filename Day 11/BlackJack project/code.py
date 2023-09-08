import random 
from replit import clear
############### Blackjack Project #####################


#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

def calculate_score(lst):

    if sum(lst) == 21 and len(lst)==2:
        return 0
    if 11 in lst and sum(lst)>21:
        lst.remove(11)
        lst.append(1)

    return sum(lst)


#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

def play_game():
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_is_over = False 
    while game_is_over!=True:
            
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"User score: {user_score}, cards={user_cards}")
        print(f"computer score: {computer_score}, cards={computer_cards}")

        if user_score ==0 or computer_score == 0 or user_score > 21 or computer_score >21:
            game_is_over = True 
        else:
            user_input = input("Do u wanna take another card? type 'y' or 'n :")
            if user_input == 'y':
                user_cards.append(deal_card())
            else:
                game_is_over = True 


    while computer_score !=0 and computer_score < 17 :
        computer_cards.append(deal_card())
        computer_score = sum(computer_cards)

    def compare(user_score,computer_score):

        print(f"Your Final Score: {user_score}, Final hand: {user_cards}")
        print(f"Computer Final Score: {computer_score}, Final hand: {computer_cards}")


        if user_score == 0:
            print("Jackblack !!! You Win")
        elif computer_score == 0:
            print("jackblack !!! Computer Win")


        if user_score > computer_score and user_score <21 and computer_score <21:
            print("You win")
        elif user_score < computer_score and user_score <21 and computer_score <21:
            print("Computer Win")

        if user_score >21 :
            print("Computer Win")
        elif computer_score >21:
            print("You Win")

        if user_score == computer_score:
            print("Draw")

    compare(user_score,computer_score)

    



while input("Do u want to play BlackJack game?")=='y':
    clear()
    play_game()
    
   



#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.