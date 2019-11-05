import turtle

screen = turtle.Screen()
screen.bgcolor("purple")
screen.title("Drawing Practice")

bob = turtle.Turtle()
bob.pensize(5)

# bob.left(360/3)
# bob.forward(100)
# bob.left(360/3)
# bob.forward(100)
# bob.left(360/3)
# bob.forward(100)

def draw_triangle(t):
  for i in range(0, 3):
    t.left(360 / 3)
    t.forward(100)

# draw_triangle(bob)
bob.hideturtle()


# bob.left(360/4)
# bob.forward(100)
# bob.left(360/4)
# bob.forward(100)
# bob.left(360/4)
# bob.forward(100)
# bob.left(360/4)
# bob.forward(100)

def draw_square(t):
  for i in range(0, 4):
    t.left(360/4)
    t.forward(100)

# draw_square(bob)



def draw_polygon(my_turtle, number_of_sides, side_length, fill_color):
  my_turtle.fillcolor(fill_color)
  my_turtle.begin_fill()
  for i in range(0, number_of_sides):
    my_turtle.left(360/number_of_sides)
    my_turtle.forward(side_length)
  my_turtle.end_fill()

# draw_polygon(bob, 3, 100, "yellow")
# draw_polygon(bob, 4, 100, "red")
# draw_polygon(bob, 5, 100, "blue")
# draw_polygon(bob, 6, 100, "green")
# draw_polygon(bob, 7, 100, "orange")
# draw_polygon(bob, 8, 100, "turquoise")

print("Hi - I am going to draw you a polygon!")
a = int(input("Please enter the number of sides: "))
b = int(input("Please enter the length of the sides: "))
c = input("Please enter the color you would like: ")
draw_polygon(bob, a, b, c)
screen.exitonclick()