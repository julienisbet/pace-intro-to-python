# create variable max_so_far, set it equal to None
# loop through every number in pile
#  if the number is even, then:
#    if max_so_far is None, then:
#       replace value of max_so_far with number
#     else
#       check if number > max_so_far:
#         replace value of max_so_far with number

pile = [82, 14, 37, 1, 9, 15, 144, 28, 96, 72, 84]
max_so_far = None
for number in pile:
  if number % 2 == 0:
    if max_so_far is None or number > max_so_far:
      max_so_far = number

print(max_so_far)








