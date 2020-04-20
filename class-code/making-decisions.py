my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_greater_than_five = []

for i in my_numbers:
    if i > 5:
        numbers_greater_than_five.append(i)

print(numbers_greater_than_five)

# conditional operators
# > < >= == !=
# logical operators - used to combine multiple conditional statements
# and or

# i > 5 is called a conditional statement
# conditionals result in the value true or false - in python, to represent true/false
# lets go into the shell and play around with some other conditional statements
# talk about Booleans
# talk about other conditions
# equality
# not equals
# string equality
# lists


pizza_toppings = ["cheese", "pepperoni", "mushrooms"]
print("We have the following toppings available:")
for topping in pizza_toppings:
    print(topping)


# we want to display the cost of the toppings
# cheese is included in the price, pepperoni and mushrooms cost $1.00
pizza_toppings = ["cheese", "pepperoni", "mushrooms"]
print("We have the following toppings available:")
for topping in pizza_toppings:
    if topping == "cheese":
        print(f"{topping} (free)")
    else:
        print(f"{topping} ($1.00)")

        #controlling the flow of your program based on the conditions of your data is an important part of programming


# Expected Output of the Program

# Welcome to Julie's Pizzeria
# Our Available Toppings Are:
# Cheese (Free)
# Pepperoni ($1 extra)
# Mushrooms (#1 extra)


pizza_toppings = ["cheese", "pepperoni", "mushrooms"]


def get_price_string(topping):
    if topping == "cheese":
        return "(Free)"
    else:
        return "($1 extra)"

# print(get_price_string("cheese") == "(Free)")
# print(get_price_string("pepperoni") == "($1 extra)")
# print(get_price_string("mushrooms") == "($1 extra)")


def print_menu(toppings):
    print("Welcome to Julie's Pizzeria")
    print("Our available toppings are:")
    for topping in toppings:
        print(f"{topping.title()} {get_price_string(topping)}")


print_menu(pizza_toppings)