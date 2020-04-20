# I'm going to be talking a lot about data types in these first few weeks
# when programming, we're generally going to be processing information
# Python needs to know what type of information that is, in order to know what to do with it

# Lets open up the Python shell in IDLE and play around with numbers.
# The first type of number we'll work with is integers
1
10
4382780
# Integers are just numbers that don’t have a decimal point.
# You can do basic calculations such as addition calculations
1 + 2
3 + 2
3 - 2
3 * 2
3 / 2
# floats
4 / 2 # also returns a float
4 + 2.0 # returns a float

## Integer division

5 // 3

## Modulo

5 % 3

# converting strings to integers and back
type(1234)
type(1234.5)
type(input())

a = int(input(a))
b = str(1)
print(type(b))