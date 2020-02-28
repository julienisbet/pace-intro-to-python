import turtle

class Coordinate:
  '''Coordinate class represents x, y coordinates'''
  def __init__(self, x=0, y=0, heading=0):
    self.x = x
    self.y = y
    self.heading = heading
  
  def quadrant(self):
    if self.x < -100:
      x_quad = -1
    elif self.x < 100:
      x_quad = 0
    else:
      x_quad = 1

    if self.y < -100:
      y_quad = -1
    elif self.y < 100:
      y_quad = 0
    else:
      y_quad = 1

    return(x_quad, y_quad)

  def drawing_coordinate(self):
    return Coordinate(self.quadrant()[0]*200, self.quadrant()[1]*200 - 36)

class GameBoard:
  '''Controls Game Board'''

  def __init__(self, size=5, shape="circle", color="black", speed=0):
    self.screen = turtle.Screen()
    self.screen.screensize(800,800)
    self.screen.title("Tic Tac Toe")

    self.pen = turtle.Turtle()
    self.pen.pensize(size)
    self.pen.color(color)
    self.pen.shape(shape)
    self.pen.speed(speed)
    self.pen.hideturtle()
    
  def move_to(self, coordinate):
    self.pen.up()
    self.pen.goto(coordinate.x, coordinate.y)
    self.pen.down()

  def draw(self):
    board_coords = [
      Coordinate(-100, 300, 270),
      Coordinate(100, 300, 270),
      Coordinate(-300, 100, 0),
      Coordinate(-300, -100, 0)
    ]
    for c in board_coords:
      self.pen.setheading(c.heading)
      self.move_to(c)
      self.pen.forward(600)

  def write(self, text, c):
      self.move_to(c)
      self.pen.write(text, move=False, align="center", font=("Arial", 36, "bold"))


class TicTacToe():
  def __init__(self):
    self.board = GameBoard()
    self.current_player = "X"
    self.next_player = "O"
    self.board_state = {}
    for i in [-1,0,1]:
      for j in [-1,0,1]:
        self.board_state[(i, j)] = ' '
  
  def play(self):
    self.board.draw()
    self.board.screen.onclick(self.record_move)

  def current_player_is_winner(self):
    print("in current_player_is_winner")
    print(self.board_state)
    return ((self.board_state[((-1,1))] == self.board_state[(0,1)] == self.board_state[(1,1)] == self.current_player) or # Across the top
          (self.board_state[(-1,0)] == self.board_state[(0,0)] == self.board_state[(1,0)] == self.current_player) or # Across the middle
          (self.board_state[(-1,1)] == self.board_state[(0,1)] == self.board_state[(1,1)] == self.current_player) or # Across the bottom
          (self.board_state[((-1,1))] == self.board_state[(-1,0)] == self.board_state[(-1, -1)] == self.current_player) or # Down the left
          (self.board_state[(0,1)] == self.board_state[(0,0)] == self.board_state[(0,-1)] == self.current_player) or # Down the middle
          (self.board_state[(1,1)] == self.board_state[(1,0)] == self.board_state[(1,-1)] == self.current_player) or # Down the right
          (self.board_state[(-1,1)] == self.board_state[(0, 0)] == self.board_state[(1, -1)] == self.current_player) or # Diagonal
          (self.board_state[(-1,-1)] == self.board_state[(0,0)] == self.board_state[(1,1)] == self.current_player))   # Diagonal
    
  def scratch_game(self):
    return not ' ' in self.board_state.values()

  def record_move(self, x, y):
    click = Coordinate(x, y)
    if self.board_state[click.quadrant()] == " ":
      self.board.write(self.current_player, click.drawing_coordinate())
      self.board_state[click.quadrant()] = self.current_player
      if self.current_player_is_winner():
        self.board.write(f"{self.current_player} WINS!", Coordinate(0, -300))
      elif self.scratch_game():
        self.board.write("SCRATCH GAME", Coordinate(0, -300))
      else:
        self.current_player, self.next_player = self.next_player, self.current_player


game = TicTacToe()
game.play()
turtle.done()
