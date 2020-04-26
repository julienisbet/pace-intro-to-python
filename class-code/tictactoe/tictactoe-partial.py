# PSEUDOCODE
# create a variable called board initialized as dictionary with 9 keys 1-9
# create a variable called active, set it true
# create a variable called current_player, set it to 'X'
# create a variable called next_player, set it to 'O'
# while active is true
  # print the board
  # create a variable called valid_move, set it to false
  # while valid_move is false
    # ask current player to pick a move
    # if move is valid
    #  update the board (set key at input to current_player)
    #  set valid_move to true
    # if player has won -- print message, set active to false
    # else if the board is full -- print message, set active to false
    # else switch current player and next player


board = {
    '1': 'O',
    '2': ' ',
    '3': ' ',
    '4': ' ',
    '5': 'X',
    '6': ' ',
    '7': 'X',
    '8': ' ',
    '9': 'O'
}

def print_board():
    print(f"""
       {board['1']} | {board['2']} | {board['3']} 1 2 3
       --+---+--
       {board['4']} | {board['5']} | {board['6']} 4 5 6
       --+---+--
       {board['7']} | {board['8']} | {board['9']} 7 8 9
    """)

print_board()
