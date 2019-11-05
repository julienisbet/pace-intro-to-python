# def print_numbers(a, b):
#   if a > b:
#     for i in range(a, b+1):
#       print(i, end = ' ')
#   else:
#     for i in range(a, b+1):
#       print(i, end = ' ')

# print_numbers(2, 7)

def print_numbers(a, b):
  if a < b:
    for i in range(a, b+1):
      print(i, end = ' ')
  else:
    for i in range(a, b-1, -1):
      print(i, end = ' ')
  print("")

print_numbers(8,5)
print_numbers(2,5)