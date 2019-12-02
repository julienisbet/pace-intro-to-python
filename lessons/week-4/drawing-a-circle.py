import turtle

screen = turtle.Screen()
screen.title("Drawing Circles Practice")

my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.color("red")
my_turtle.fillcolor("red")
my_turtle.begin_fill()
my_turtle.circle(100)
my_turtle.right(100)
my_turtle.circle(100)
my_turtle.right(100)
my_turtle.circle(100)
my_turtle.right(100)
my_turtle.circle(100)
my_turtle.end_fill()


turtle.done()