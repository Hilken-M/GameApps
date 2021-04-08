##Initialize
import random
    ##Create Board
        ##3x3 grid
def display_board(board):
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[1]+'|'+board[2]+'|'+board[3])
        ## Values to be replaced 

    ##Create Markers
def player_input():
    marker = ' '

    while marker != 'X' and marker !='O':
        marker = input('Player1: Choose X or O ').upper()

    if marker == 'X':
        return ('X', 'O')
    else: 
        return ('O','X')
        ##Player 1
        ##Player 2

    ##Decide Who goes first
        ##random.choice()
def choose_first():
    if random.randint(0,1) ==0: 
        return 'Player 2'
    else: 
        return 'Player 1'

##Players need to be able to take turns
    ##display board state - use f strings to show marker postion board  
    ##receive input
def player_choice(board):

    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
    return position
    
    ##update board state with markers
def space_check(board, position):
    return board[position]== ' '

def place_marker(board, marker, position):
    board[position] = marker
    ##Check for end condition

##End Conditions: 
def win_check(board, mark):
        # horizontal 
    return((board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
        # vertical
    (board[1]== mark and board[4]== mark and board[7]== mark) or
    (board[2]== mark and board[5]== mark and board[8]== mark) or
    (board[3]== mark and board[6]== mark and board[9]== mark) or
        # diagnal 
    (board[1]== mark and board[5]== mark and board[9]== mark) or
    (board[3]== mark and board[5]== mark and board[7]== mark))
        # tie
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
        # Board is full if we return true
    return True

##Conclusion
    #Congratualte the winner
    #Display board state
    #Play again? y/n
def replay():
    return input("Play again? Enter Y or N: ").upper
    


## Setup (Board, Whos First, Choose markers X,0)
while True:
    theboard = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? Y or N? ').upper()

    if play_game == 'Y':
        game_on = True
    else: 
        game_on = False

## Game Play
    while game_on:
    ### Player One Turn
        if turn == 'Player 1':
        # Show the board
            display_board(theboard)
        # Choose a position
            position = player_choice(theboard)
        # Place the marker on the position
            place_marker(theboard,player1_marker,position)
        # Check if they won
            if win_check(theboard,player1_marker):
                display_board(theboard)
                print("Player 1 has won!!")
                game_on = False
            else:
                # Or check if there is a tie
                if full_board_check(theboard):
                    display_board(theboard)
                    print("Tie Game")
                    break
                else:
                    # No tie and no win? Then next player's turn
                    turn = 'Player 2'
        else:
    ### Player Two Turn
    # Show the board
            display_board(theboard)
        # Choose a position
            position = player_choice(theboard)
        # Place the marker on the position
            place_marker(theboard,player2_marker,position)
        # Check if they won
            if win_check(theboard,player2_marker):
                display_board(theboard)
                print("Player 1 has won!!")
                game_on = False
            else:
                # Or check if there is a tie
                if full_board_check(theboard):
                    display_board(theboard)
                    print("Tie Game")
                    break
                else:
                    # No tie and no win? Then next player's turn
                    turn = 'Player 1'
    if not replay():
        break 
        