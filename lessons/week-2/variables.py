# In this example, I have printed some information about my dog.
# Notice how the word Benny appears twice
print("My dog’s name is Benny. Benny is a very cute")

# What is I wanted to change this to a different dog's name
# I would need to change the word Benny is two places
# In this example, thats not a big deal but you can imagine if we can a program
# That was hundreds of lines long or spanned multiple files
# It would be very error-prone to do a find and replace on that word
# Instead lets use a variable

# Think of a variable as a box that we’re using the store information
# We can give it a label so that we know what kind of information is in the box
# We can also swap out the contents of the box as necessary

# In python, declaring variables is as simple as deciding on a name and then using a single equals sign to assign that variable a value.
# In this example, let’s call our variable dog_name. We can now print that the same way that we printed other strings. 

dog_name = "Benny"
print(dog_name)

# we're telling python to take the string Benny, store it in memory, and give it a label called dog_name
# Great - so now we have a variable storing our information
# but how do we include it within a string? 
# For that we’ll use an f-string which stands for format
# F-strings allow us to embed the variable within the string.

print(f"My dog’s name is {dog_name}. {dog_name} is very cute :)")
# if I wanted to change this to a different dog
# I would now only need to do it in one place. 

# Naming rules
# Must only contain letters, numbers and underscores
# Cannot start with a number
# Spaces are not allowed
# Avoid Python keywords
  
# Common errors:
# Misspelling your variable names
# Forgetting quotation marks on strings

print("Please enter your name: ")
a = input()
print(f"Hello, {a}!")