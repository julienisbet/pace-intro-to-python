import turtle

screen = turtle.Screen()
screen.bgcolor("#9EC388")
screen.title("Drawing Circles Practice")

my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.color("#AD0509")
my_turtle.fillcolor("#FBC70F")
my_turtle.begin_fill()
my_turtle.circle(100)
my_turtle.end_fill()


turtle.done()