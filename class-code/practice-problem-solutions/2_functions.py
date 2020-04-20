#==============================================================================#
# PART ONE
#==============================================================================#

# Write a function called cube that accepts an integer, and prints out 
# the cube of that integer

def cube(n):
  print(n**3)

cube(3)

# Write a function called describe_city that accepts the name of a city 
# and its country. The function should print a simple sentence, such as
# “Reykjavik is in Iceland”. Give the parameter for the country a default value. 
# Call your function for three different cities, at least one of which is not 
# in the default county.

def describe_city(city="Goleta", country="United States"):
  print(f"{city} is in {country}")

describe_city("Glasgow", "Scotland")

# Write a function called get_formatted_name that accepts a first_name
# and last_name as required parameters and a third parameter called middle_name
# which is optional. The function should print the first, middle and last names
def get_formatted_name(first_name, last_name, middle_name=""):
  middle_name = f" {middle_name} ".replace("  ", " ")
  print(f"{first_name.title()}{middle_name.title()}{last_name.title()}")

get_formatted_name("Julie", "Nisbet")
get_formatted_name("julie", "nisbet")
get_formatted_name("julie", "nisbet", "mary")

#==============================================================================#
# PART TWO
#==============================================================================#

# Create a function called `square` that takes a number as an argument
# and returns the square

def square(n):
  return n*n

two_squared = square(2)
print(two_squared)

# Using the above function, print the result of 2 squared plus 3 squared
print(square(2) + square(3))

# Create a function called get_c_temp that accepts a single argument
# fahrenheit and returns the value of the fahrenheit temperature in celsius.
# Note, C = (F - 32)*(5/9)
def get_c_temp(f_temp):
  return (f_temp - 32) * (5 / 9)

# Create a function called get_k_temp that accepts a single argument celsius
# and returns the value of the celsius temperature in kelvin. 
# Note, K = C + 273.15

def get_k_temp(c_temp):
  return c_temp + 273.15

# Using the two temperature functions, find the value in Kelvin 
# of 45 degrees fahrenheit

c_temp = get_c_temp(45)
k_temp = get_k_temp(c_temp)
print(k_temp)

# OR

k_temp = get_k_temp(get_c_temp(45))
print(k_temp)
