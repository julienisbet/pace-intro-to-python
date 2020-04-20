# Given a two-digit integer, print its left digit (a tens digit)
# and then its right digit (a ones digit). Use the operator of
# integer division for obtaining the tens digit and the
# operator of taking remainder for obtaining the ones digit.
# Sample Input 
# 78
# Expected Output 
# 7 8
digits = int(input("Please enter a 2 digit number: "))
tens = digits // 10
ones = digits % 10
print(f"{tens} {ones}")

# Given a two-digit integer, swap its digits and print the result.
# Sample Input 
# 78
# Expected Output 
# 87
print(f"{ones}{tens}")
# or, if you want an integer
print(ones*10 + tens)

# Given an integer, print its tens digit.
# Sample Input
# 1234
# Expected Output 
# 3

num = int(input("Please enter a number: "))
print(num % 100 // 10)

# Create a program that asks for a person's name and eye color then prints them back to them
# Sample Input
# Julie
# blue
# Expected Output
# Hello, Julie. You have blue eyes.
name = input("Please enter your name: ")
eye_color = input("Please enter your eye color: ")
print(f"Hello, {name.capitalize()}. You have {eye_color} eyes.")

# Write a program that will input °C and output °F.
# A second program will input °F and output °C. °F = °C * 9/5 + 32
# Sample Input 
# Please enter celcius: 0
# Sample Output
# 0 C is 32 F
celcius = int(input("Please enter celcius: "))
faranheit = celcius * (9/5) + 32
print(f"{celcius} C is {round(faranheit,2)} F")

# Write a program that reads the length of the base and the height of a right-angled triangle and prints the area. Every number is given on a separate line.
a = int(input("Please enter length: "))
b = int(input("Please enter height: "))
print(f"The area of this triangle is {a*b/2}")