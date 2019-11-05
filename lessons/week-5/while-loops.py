# current_number = 1
# while current_number = 5:
#   print(current_number)
#   current_number += 1


prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program.\n"
# Approach 1
# message = ""
# while message != 'quit':
#   message = input(prompt)
#   if message != 'quit':
#     print(message)

# Approach 2
# program_active = True
# while program_active:
#   message = input(prompt)
#   if message == 'quit':
#     program_active = False
#   else:
#     print(message)

# Using breaks

while True:
  message = input(prompt)
  if message == 'quit':
    break
  print(message)

# https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/RandomlyWalkingTurtles.html