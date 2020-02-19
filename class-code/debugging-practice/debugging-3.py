# The function string_counter should return the number
# of times the second argument appears in the first argument
# The program is currently showing None instead of the expected value 4
# Can you update it to make it work?
 

def string_counter(str_1, str_2="a"):
  result = str_1.count(str_2)

print(string_counter("aaaa"))