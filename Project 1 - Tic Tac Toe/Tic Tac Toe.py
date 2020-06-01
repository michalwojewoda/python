#starting with creation of a board 
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


