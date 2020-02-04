import turtle
sides = int(input("How many sides would you like? "))
color = input("Which color would you like? ")

screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.color(color)

angle = 360 / sides
for i in range(0, sides):
  my_turtle.forward(100)
  my_turtle.right(angle)

turtle.done()
