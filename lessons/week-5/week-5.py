import turtle

def draw_triangle(t):
  for i in range(3):
    t.left(120)
    t.forward(200)

# draw_triangle(bob)
# bob.goto(250, 250)
# draw_triangle(bob)

def draw_polygon(t, number_of_sides, side_length, border_color, fill_color):
  t.color(border_color)
  t.fillcolor(fill_color)
  t.begin_fill()
  for i in range(number_of_sides):
    t.left(360/number_of_sides)
    t.forward(side_length)
  t.end_fill()

print("Welcome to Polygon Drawer")
n = int(input("How many sides would you like me to draw? "))
l = int(input("How long are the sides?"))
c = input("What color is the border?")
fc = input("What color is the fill?")
screen = turtle.Screen()
screen.bgcolor("purple")

bob = turtle.Turtle()
bob.pensize(5)

draw_polygon(bob, n, l, c, fc)
screen.exitonclick()

