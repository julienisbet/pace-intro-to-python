# one the things computers are best used for is automating tedious tasks
# example -- sending a message to everyone in a list

pizza_toppings = ["cheese", "pepperoni", "mushrooms"]
print(pizza_toppings)
# note that python prints the list format


pizza_toppings = ["cheese", "pepperoni", "mushrooms"]
for topping in pizza_toppings:
    print(topping)
# note that the word topping is not special - you can use any variable you want
# you want your programs to be readible so you'll want to
# use a variable name that is representative of the data you are working with


# lets do more than just print the topping
pizza_toppings = ["cheese", "pepperoni", "mushrooms"]
for topping in pizza_toppings:
    message = f"I would like {topping} on my pizza please."
    print(message)


# Using ranges
for value in range(1, 5):
  print(value)
# note: doesn't print 5
# convert to list
a = list(range(1, 5))

even_numbers = list(range(2, 11, 2))

max(a)
min(a)
sum(a)

squares = [value**2 for value in range(1, 11)]
a = [int(s) for s in input().split()]

