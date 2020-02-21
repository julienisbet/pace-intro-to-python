import turtle
import random

screen = turtle.Screen()
screen.bgcolor("#9EC388")
screen.title("Event Driven Programming")
screen.screensize(600,600)

# KEY EVENTS
t = turtle.Turtle()
def draw_a():
  t.write("A", move=False, align="center", font=("Arial", 36, "bold"))
  a = random.randint(-300,300)
  b = random.randint(-300,300)
  print(f"moving turtle: {a}, {b}")
  t.goto(a, b)

screen.listen()
screen.onkeypress(draw_a, key="a")
turtle.done()

# CLICK EVENTS
benny = turtle.Turtle()
benny.color("purple")
benny.shape("turtle")
finley = turtle.Turtle()             # Move them apart
finley.color("blue")
finley.shape("turtle")
finley.penup()
finley.goto(0, 100)
finley.pendown()

def benny_handler(x, y):
    screen.title("Benny clicked at {0}, {1}".format(x, y))
    benny.forward(30)

def finley_handler(x, y):
    screen.title("Finley clicked at {0}, {1}".format(x, y))
    finley.forward(50)

benny.onclick(benny_handler)
finley.onclick(finley_handler)

turtle.done()
