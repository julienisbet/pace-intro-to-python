# import turtle

# screen = turtle.Screen()
# screen.title("Drawing Circles Practice")

# my_turtle = turtle.Turtle()
# my_turtle.pensize(5)
# my_turtle.color("red")
# my_turtle.fillcolor("red")
# my_turtle.begin_fill()
# my_turtle.circle(100)
# my_turtle.right(100)
# my_turtle.circle(100)
# my_turtle.right(100)
# my_turtle.circle(100)
# my_turtle.right(100)
# my_turtle.circle(100)
# my_turtle.end_fill()


# turtle.done()


import turtle

# we then need to make a new drawing screen
# we do this by using the  screen function

screen = turtle.Screen()
screen.bgcolor("#9EC388")
screen.title("Drawing Lines Practice")

my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.shape("circle")


for x in range(0, 8):
    my_turtle.pendown()
    my_turtle.left(45)
    my_turtle.forward(100)
    my_turtle.penup()
    my_turtle.backward(100)

my_turtle.hideturtle()
turtle.done()
