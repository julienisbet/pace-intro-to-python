import turtle

def move_turtle(t, x, y):
    t.up()
    t.goto(x, y)
    t.down()

def draw_board(t):
  board_coords = [
    {'x': -100, 'y': 300, 'heading': 270},
    {'x': 100, 'y': 300, 'heading': 270},
    {'x': -300, 'y': 100, 'heading': 0},
    {'x': -300, 'y': -100, 'heading': 0}
  ]
  for coords in board_coords:
    t.setheading(coords['heading'])
    move_turtle(t, coords['x'], coords['y'])
    t.forward(600)

quadrants = {
  (-200, 150): "1",
  (0, 150): "2",
  (200, 150): "3",
  (-200, -36): "4",
  (0, -36): "5",
  (200, -36): "6",
  (-200, -250): "7",
  (0, -250): "8",
  (200, -250): "9",
}

def record_move(x,y):
  global current_player
  global next_player
  if x < -100:
    x_coor = -200
  elif x < 100:
    x_coor = 0
  else:
    x_coor = 200
  
  if y < -100:
    y_coor = -250
  elif y < 100:
    y_coor = -36
  else:
    y_coor = 150
  quad = quadrants[(x_coor, y_coor)]
  if game_board[quad] == " ":
    print_move(x_coor, y_coor, current_player)
    game_board[quad] = current_player
    if is_winner(game_board, current_player):
      move_turtle(my_turtle, 0, -300)
      my_turtle.write(f"{current_player} WINS!", move=False, align="center", font=("Arial", 36, "bold"))
      turtle.done()
    elif not ' ' in game_board.values():
      move_turtle(my_turtle, -300, -300)
      my_turtle.write(f"SCRATCH GAME", move=False, align="center", font=("Arial", 36, "bold"))
    else:
      current_player, next_player = next_player, current_player

def print_move(x, y, player):
  move_turtle(my_turtle, x, y)
  my_turtle.write(player, move=False, align="center", font=("Arial", 72, "bold"))
  move_turtle(my_turtle, 0, 0)

def is_winner(b, player):
  return ((b['1'] == b['2'] == b['3'] == player) or # Across the top
          (b['4'] == b['5'] == b['6'] == player) or # Across the middle
          (b['7'] == b['8'] == b['9'] == player) or # Across the bottom
          (b['1'] == b['4'] == b['7'] == player) or # Down the left
          (b['2'] == b['5'] == b['8'] == player) or # Down the middle
          (b['3'] == b['6'] == b['9'] == player) or # Down the right
          (b['3'] == b['5'] == b['7'] == player) or # Diagonal
          (b['1'] == b['5'] == b['9'] == player))   # Diagonal

SPACES = list('123456789')
game_board = {}
for s in SPACES:
  game_board[s] = ' '
active = True
current_player = 'X'
next_player = 'O'

screen = turtle.Screen()
screen.screensize(800,800)
screen.title("Tic Tac Toe")

my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.color("black")
my_turtle.shape("circle")
my_turtle.speed(0)

draw_board(my_turtle)
screen.onclick(record_move)
turtle.done()
