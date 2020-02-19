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


def print_board(b):
  print(f'''
    {b['1']} | {b['2']} | {b['3']} 1 2 3
    --+---+--
    {b['4']} | {b['5']} | {b['6']} 4 5 6
    --+---+--
    {b['7']} | {b['8']} | {b['9']} 7 8 9
  ''')

def check_winner(b, player):
  pass

def check_board_full(b):
  pass

# print_board(game_board)
# game_board['1'] = 'X'
# game_board['5'] = 'O'
# print(game_board)
# print_board(game_board)

active = True
current_player = "X"
next_player = "O"
SPACES = list('123456789')
game_board = {}
for s in SPACES:
  game_board[s] = " "

while active:
  print_board(game_board)
  valid_move = False
  while not valid_move:
    space = input("Please enter a space 1-9 \n")
    if space in SPACES and game_board[space] == " ":
      game_board[space] = current_player
      valid_move = True
    else:
      print("Sorry, that's not a valid space. Please try again.")
  if check_winner(game_board, current_player):
    print("yay")
  elif check_board_full(game_board):
    print("boo")
  else:
    current_player, next_player = next_player, current_player



