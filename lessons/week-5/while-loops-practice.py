# current_number = 1
# while current_number < 5:
#   print(current_number)
  # current_number += 1

prompt = """
          Tell me something and I will repeat it back to you!"
          Enter 'gobyebye' to end the program
        """

message = ""

# while message != "gobyebye":
#   message = input(prompt)
#   if message != 'gobyebye':
#     print(message)

active = True
while active:
  message = input(prompt)
  if message == "quit":
    active = False
  else:
    print(message)










