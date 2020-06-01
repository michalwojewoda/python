#starting with creation of a board 
import random

def display_board(board):
    print('\n'*100)
    print("    |     |   ")
    print(" "+board[1]+"  |  "+board[2]+"  |  "+board[3])
    print("----|-----|----")
    print(" "+board[1]+"  |  "+board[2]+"  |  "+board[3])
    print("----|-----|----")
    print(" "+board[1]+"  |  "+board[2]+"  |  "+board[3])
    print("    |     |   ")

board = ["#","0","0","0","0","0","0","0","0","0"]
print(display_board(board))
print(display_board(board))

#assign players

def player_input():

    '''
    Output is tuple = (player 1 marker, Player 2 marker)

    '''
    marker = ""
    while marker != 'X' and marker !='O':
        marker = input("Player 1, choose X or O: ").upper()
    
    if marker == "x":

        return ("X", "O")
    else: 
        return("O","X")

#Write function that takes in the board list object, a marker, and desired position number 1-9 and assign it to the board.

def place_marker(board, marker,position):

    board[position] = marker 

# write a function tat takes in a board and mark x o and then checks to see if that mark has won

def win_check(board, mark):

    # return boolean to check if true or false

    return ((board[7] == board[8] == board[9] == mark) or # across
    (board[4] == board[5] == board[6] == mark) or # across
    (board[1] == board[2] == board[3] == mark) or #across 
    (board[7] == board[4] == board[1] == mark) or #down
    (board[8] == board[5] == board[2] == mark) or # down
    (board[9] == board[6] == board[3] == mark) or # down
    (board[7] == board[5] == board[3] == mark) or #diagonal
    (board[9] == board[5] == board[1] == mark) #Diagonal

# Random module - to randomly choose player that goes first

import random

def choose_first():

    flip = random.randint(0,1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

# booleaon that indicate free space on the board

def space_check(board, position):

    return board[position] == " "

#check if the board is fulli