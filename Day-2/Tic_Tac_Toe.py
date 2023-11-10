from replit import clear
board = [[1,2,3],[4,5,6],[7,8,9]]

lst = []

def checkVertical(board):
    if board[0][0] == board[1][0] == board[2][0] or board[0][1] == board[1][1] == board[2][1] or board[0][2] == board[1][2] == board[2][2]:
        return 1 
def checkHorizontal(board):
    if board[0][0] == board[0][1] == board[0][2] or board[1][0] == board[1][1] == board[1][2] or board[2][0] == board[2][1] == board[2][2]:
        return 1
def checkDiagonal(board):
    if board[0][0] == board[1][1] == board[2][2] or board[0][2]==board[1][1]==board[2][0]:
        return 1 

def placeOnBoard(board,inp,sign):
        for row in range(len(board)):
            for col in range(len(board[0])):
                    if board[row][col] == inp:
                        board[row][col] = sign  
                        
                

def printBoard(board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                print(board[row][col],end=' | ')
                
            print()
            print('-- ---  --')

total_turn = 9 
game_is_on = True 

first_player_turn = True 
Second_player_turn = False 

while game_is_on and total_turn!=0:
    
    if first_player_turn == True:
        inp = int(input("1st player turn('X'). Enter position "))
        if inp not in lst:
            placeOnBoard(board,inp,"X")
            clear()
            printBoard(board)
            lst.append(inp)
            total_turn-=1
            first_player_turn = False 
            Second_player_turn = True  
        else:
             print(f"{inp} pos is already filled up. Enter in empty location")

        if checkDiagonal(board) == 1 or checkHorizontal(board) == 1 or checkVertical(board)==1:
            clear()
            print(f"Game Over. First Player Win!")
            printBoard(board)
            game_is_on = False 

    
    elif  Second_player_turn == True:
        inp = int(input("2nd player turn('O') . Enter position "))
        if inp not in lst:
            placeOnBoard(board,inp,"O")
            lst.append(inp)
            clear()
            printBoard(board)
            total_turn-=1
            first_player_turn = True  
            Second_player_turn = False 
        else:
             print(f"{inp} pos is already filled up. Enter in empty location")
        
        if checkDiagonal(board) == 1 or checkHorizontal(board) == 1 or checkVertical(board)==1:
            clear()
            print(f"Game Over. 2nd Player Win!")
            printBoard(board)
            game_is_on = False 



if total_turn == 0:
    print("Match Draw")
    printBoard(board)


    




