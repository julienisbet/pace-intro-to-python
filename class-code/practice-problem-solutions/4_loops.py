# Use the range function to create a list of all odd numbers
# between 100 and 200
print(list(range(101, 200, 2)))

# What is the sum of all digits between 1 and 1 million?
print(sum(range(1, 1_000_001)))

# Using range and a for loop, print all multiples of 3 between 3 and 30
for i in range(3, 31, 3):
  print(i)

# Using range(1, 11), create a list called squares that contains the
# squares of every integer between one and 10
squares = []
for i in range(1, 11):
  squares.append(i*i)
print(squares)
# OR
squares = [i*i for i in range(1, 11)]
print(squares)

# Last week we wrote a program that accepted two inputs representing
# height and width, and output the area of a rectangle. Modify that 
# program to now accept a single input, with the values separated with a space. 
# Convert the string into a list using the split function. 
# Then return the product of the two values.

def get_area(string_data):
 data = [int(s) for s in string_data.split()]
 return data[0] * data[1]

print(get_area("2 4"))

