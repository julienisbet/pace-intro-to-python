# functions are named blocks of code
# if you want to peform the particular behavior you've
# defined in the code, we "call" the function
# allows you to isolate behavior and reduce repetitiveness
# For example, lets print a simple message to the screen
print("Hello!")


# Lets move this into a function
# keyword "def" tells python you are defining a function
# parentheses allows you to pass information needed to do its job
# real world example: 
def say_hello():
    print("Hello!")

# When we want to perform the behavior defined by the function, 
# we say that we call the function. 

say_hello()

# This is the simplest structure of a function but they will all follow
# this structure-- we start with the key word def then we name the function
# followed by parentheses and a colon. All of the content inside of the
# function needs to be indented.

# Note that our parentheses are empty for now, because this function does
# not accept any arguments meaning it doesn’t need any additional information
# to do its job. Using our cheeseburger analogy, this is like saying there are
# no substitutions allowed on the burger - if you order a burger,
# you’ll always get the same burger back. What if, however you had to specify
# what type of cheese you wanted on the burger. In this situation, the chef
# needs additional information in order to carry out the behavior of making
# a burger.  Let’s change that by updating this functions job from just saying
# hello generically, to saying hello to a specific user.
# We do that by adding a parameter inside the parentheses which we’ll call name


def say_hello(name):
    print(f"Hello {name}!")


say_hello("Benny")

# can have multiple  arguments

def describe_yourself(name, age):
    print(f"My name is {name} and I am {age} years old.")
describe_yourself("Julie", 21)
# these arguments are called positional arguments -- you pass up the arguments in the same
# order they are defined on the function call
# reverse the order
def describe_pet(animal_type, pet_name):
  print(f"\nI have a {animal_type}\nMy {animal_type}'s name is {pet_name}\n")

describe_pet("dog", "Benny")
describe_pet("Benny", "dog")

# keyword_arguments -- definition of function doesn't change
describe_pet(pet_name="Benny", animal_type="dog")

# default arguments
def say_hello(name="world"):
  print(f"hello {name}")

say_hello()
say_hello("julie")