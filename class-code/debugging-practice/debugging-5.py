# The function string_counter should return the number
# of times the second argument appears in the first argument
# The program is currently returning 0 instead of the expected value 6
# Can you update it to make it work?
 

def string_counter(str_1, str_2):
  result = "str_1".count("str_2")
  return result

print(string_counter("aabbaabbaa", "a"))