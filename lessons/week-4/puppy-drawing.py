import turtle
wn = turtle.Screen()



def move_turtle(my_turtle, x, y):
    my_turtle.penup()
    my_turtle.goto(x, y)


def draw_line(my_turtle, heading, length, color="black"):
    my_turtle.color(color)
    my_turtle.setheading(heading)
    my_turtle.pendown()
    my_turtle.forward(length)
    my_turtle.penup()

def draw_circle(my_turtle, radius, color="black"):
    my_turtle.color(color)
    my_turtle.fillcolor(color)
    my_turtle.pendown()
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()
    my_turtle.penup()


def draw_rectangle(my_turtle, width, height, color="black"):
    my_turtle.color(color)
    my_turtle.fillcolor(color)
    my_turtle.pendown()
    my_turtle.begin_fill()
    my_turtle.forward(width)
    my_turtle.left(90)
    my_turtle.forward(height)
    my_turtle.left(90)
    my_turtle.forward(width)
    my_turtle.left(90)
    my_turtle.forward(height)
    my_turtle.left(90)
    my_turtle.end_fill()
    my_turtle.penup()


def draw_triangle(my_turtle, height, width, direction, color="black"):
    my_turtle.color(color)
    my_turtle.fillcolor(color)
    original_x = my_turtle.xcor()
    original_y = my_turtle.ycor()
    my_turtle.setheading(270)
    my_turtle.pendown()
    my_turtle.begin_fill()
    my_turtle.forward(height)

    if direction == "left":
        my_turtle.left(90)
    else:
        my_turtle.right(90)

    my_turtle.forward(width)
    my_turtle.goto(original_x, original_y)
    my_turtle.end_fill()
    my_turtle.penup()


t = turtle.Turtle()
t.pensize(5)
t.speed(8)
move_turtle(t, -110, 110)
draw_rectangle(t, 220, 185, color="#534741")
move_turtle(t, 0, -110)
draw_circle(t, 110, color="#c7b299")
move_turtle(t, -110, 0)
draw_rectangle(t, 220, 110, color="#c7b299")
move_turtle(t, 0, 0)
draw_circle(t, 110, color="#c7b299")
move_turtle(t, 0, 70)
draw_circle(t, 35)
draw_line(t, 270, 100)
move_turtle(t, t.xcor() - 25, t.ycor())
draw_line(t, 0, 50)
move_turtle(t, -55, 220)
draw_circle(t, 20)
move_turtle(t, 55, 220)
draw_circle(t, 20)
move_turtle(t, 110, 295)
draw_triangle(t, 120, 80, "left", "#534741")
move_turtle(t, 110, 280)
draw_triangle(t, 90, 60, "left", "#c7b299")
move_turtle(t, -110, 295)
draw_triangle(t, 120, 80, "right", "#534741")
move_turtle(t, -110, 280)
draw_triangle(t, 90, 60, "right", "#c7b299")

wn.mainloop()
