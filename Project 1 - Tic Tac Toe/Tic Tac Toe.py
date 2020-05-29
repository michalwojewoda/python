def display_board(board):
    print("    |     |   ")
    print(" "+board[1]+"  |  "+board[2]+"  |  "+board[3])
    print("----|-----|----")
    print(" "+board[1]+"  |  "+board[2]+"  |  "+board[3])
    print("----|-----|----")
    print(" "+board[1]+"  |  "+board[2]+"  |  "+board[3])
    print("    |     |   ")

board = ["#","0","0","0","0","0","0","0","0","0"]
print(display_board(board))