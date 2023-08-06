import random 
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#print(chosen_word)
display = ['_']*len(chosen_word)


end_of_game = False
 
lives = 6

while  end_of_game != True:
    letter = input('Enter letter:')

    for i in range(len(chosen_word)):
        if letter == chosen_word[i]:
            pos = i 

            display[pos] = letter 
    
    if '_' not in display:
        end_of_game = True
        print("You Win")
     
    if letter not in chosen_word: 
        lives-=1     
        if lives == 0:
            end_of_game = True
            print('You lose')


       
    print(' '.join(display))

         
    print(stages[lives])
     



