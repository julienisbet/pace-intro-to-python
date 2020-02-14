# PSEUDOCODE
# create a variable board initialize with dictionary with 9 keys 1-9
# create variable called active, set to true
# create a variable current_player, set to 'X', create variable next_player set it to 'O'
# while active is true
  # print the board state
  # set valid_move to none
  # while valid_move is not true
    # ask current_player to pick a square
    # check if the square is valid
    # if valid, set valid_move to true and update board
  # if player has won -- print message, set active to false
  # else if board full -- print message, set active to false
  # else set current player to other player

# Inspired by...
# Tic Tac Toe, by Al Sweigart al@inventwithpython.com
# The classic board game.

print('Welcome to Tic Tac Toe')
## GAME SETUP
SPACES = list('123456789')
game_board = {}
for s in SPACES:
  game_board[s] = ' '
active = True
current_player = 'X'
next_player = 'O'

## UTILITY FUNCTIONS
def print_board(b):
  print(f'''
    {b['1']} | {b['2']} | {b['3']} 1 2 3
    --+---+--
    {b['4']} | {b['5']} | {b['6']} 4 5 6
    --+---+--
    {b['7']} | {b['8']} | {b['9']} 7 8 9
  ''')

def is_winner(b, player):
  return ((b['1'] == b['2'] == b['3'] == player) or # Across the top
          (b['4'] == b['5'] == b['6'] == player) or # Across the middle
          (b['7'] == b['8'] == b['9'] == player) or # Across the bottom
          (b['1'] == b['4'] == b['7'] == player) or # Down the left
          (b['2'] == b['5'] == b['8'] == player) or # Down the middle
          (b['3'] == b['6'] == b['9'] == player) or # Down the right
          (b['3'] == b['5'] == b['7'] == player) or # Diagonal
          (b['1'] == b['5'] == b['9'] == player))   # Diagonal

# game_board['1'] = 'X'
# game_board['9'] = 'O'

while active:
  print_board(game_board)
  print(f"Your move {current_player}")
  valid_move = False
  while not valid_move:
    space = input("Please enter a space: 1-9\n")
    if space in SPACES and game_board[space] == " ":
      valid_move = True
      game_board[space] = current_player
    else:
      print(f"Sorry, {space} is not a valid space.")
  if is_winner(game_board, current_player):
    print_board(game_board)
    print(f"{current_player} WINS!")
    active = False
  elif not ' ' in game_board.values():
    print_board(game_board)
    print("CATS GAME!")
    active = False
  else:
    current_player, next_player = next_player, current_player
