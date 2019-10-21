def string_counter(x, y="a"):
  print(x.count(y))

string_counter("hello world", "o")
# 2
string_counter("hello world", "l")
# 3
string_counter("aaaaa")
# 5

def string_counter(x, y="a"):
  return x.count(y)

a = string_counter("hello world", "o")
print(a)
print(type(a))
print(a + 3)


# can also do 
def string_counter(x, y="a"):
  count = x.count(y)
  return count

# functions can also process some data and then return a value or a set of values
# the value it returns is called a return value
# if a function doesn't return anything, it automatically returns None


## What is wrong with the following code?
def add_xyz(x, y, z):
    return x + y + z
    print('the answer is', x + y + z)
