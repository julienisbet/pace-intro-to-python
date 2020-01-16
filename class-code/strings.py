# strings are just a list of characters in python
print("Hello")
# You can use single quotes or double quotes
print('Hello')
# You can also use a triple quote if your string is going
# to span multiple lines
print(
    ''' Dear John,
    Hello
    Etc..
    '''
)
# Whitespace characters
print("Dear John \nHello\netc")

# Generally using single or double quotes is a matter of personal preference
# If the characters you want to display include single quotes
# you need to use double quotes and vice versa
print("My dog's name is Benny")

# Python includes a number of built in functions in python
# that allow us to perform operations on strings.
# For example, if you wanted to shout my dog’s name,
# you can use the `upper` function to do that.
print("My dog’s name is Benny".upper())

# to get the length of a string use the len function
print(len('abcdefghijklmnopqrstuvwxyz'))