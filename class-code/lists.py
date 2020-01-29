numbers = [1, 2, 3, 4, 5]
pizza_toppings = ["cheese", "pepperoni", "mushrooms", "pineapple"]
mixed_array = [1, "cheese", 2, "pepperoni"]
list_of_lists = [[1, 2], [2, 3]]

# We access the individual elements of the list using something called an index
# An index just the position of an individual element
# In most programming languages, we start counting indexes zero
# The first element of the list is said to have index 0.

print(pizza_toppings[0])

# You can also count backwards from the end of the list, using a negative index
# So the last element is said to have an index of -1

print(pizza_toppings[-1])
print(pizza_toppings[-2])

# If you make a mistake and try to access an element that doesn’t exist
# Python will give you an IndexError

print(pizza_toppings[4])

## slicing lists
pizza_toppings[0:1]
pizza_toppings[:2]
pizza_toppings[1:]

## Concatenating lists
[1,2,3] + ["a", "b", "c"]
["a", "b", "c"] * 3

# It can be helpful to know exactly how many elements are in your list
# To do this we can use the len function
print(len(pizza_toppings))

# Lists are mutable in Python meaning we can change them.
# Lets do that by adding some toppings to our list of pizza toppings.
pizza_toppings.append("pineapple")
print(pizza_toppings)

pizza_toppings.insert(0, "anchovies")
print(pizza_toppings)

# We can also remove items…
del pizza_toppings[0]
print(pizza_toppings)


a = pizza_toppings.pop()
print(a)
print(pizza_toppings)

b = pizza_toppings.pop(1)
print(pizza_toppings)


pizza_toppings.remove("cheese")
print(pizza_toppings)

pizza_toppings = ["cheese", "cheese", "pepperoni"]
pizza_toppings.remove("cheese")
print(pizza_toppings)

pizza_toppings = ["pepperoni", "anchovies", "cheese"]
pizza_toppings.sort()
pizza_toppings = ["pepperoni", "anchovies", "cheese"]
sorted(pizza_toppings, reverse=True)
numbers.reverse()
