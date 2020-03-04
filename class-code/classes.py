import math

class Dog():
  '''A class for representing dogs'''
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  # every method call associated with an instance automatically passes self
  # self is a reference to the instance itself
  def bark(self):
    print(f"{self.name} says bark bark!")

benny = Dog("Benny", "Terrier Mix", 4)

print(benny.name)
benny.bark()


class Circle():
  def __init__(self, radius):
    self.radius = 10
  
  def get_area(self):
    return self.radius * self.radius * math.pi

  def get_circumference(self):
    return self.radius * 2 * math.pi

c = Circle(10)
print(c.get_area())
print(c.get_circumference())

import turtle
class Polygon():
  def __init__(self, sides):
    self.sides = sides

  def draw(self):
    angle = 360 / self.sides
    for i in range(0, self.sides):
      my_turtle.forward(100)
      my_turtle.right(angle)

class Square(Polygon):
  def __init__(self):
    super().__init__(sides=4)

class Octogon(Polygon):
  def __init__(self):
    super().__init__(sides=8)

# my_square = Square()
# my_square.draw()

screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.color("#365C8A")

my_octogon = Octogon()
my_octogon.draw()

turtle.exitonclick()