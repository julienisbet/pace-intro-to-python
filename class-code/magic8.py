
responses = [
  "It is decidedly so",
  "Yes, definitely",
  "Reply hazy, try again",
  "Ask again later",
  "Concentrate and ask again",
  "My reply is no",
  "Outlook not so good",
  "Very doubtful"
]

# print(responses[3])

# ask user for input
# generate a random integer between 0 and 7
# store integer in variable i
# print the response at integer i

import random
print("==============================")
print("WELCOME TO THE MAGIC 8 BALL!!!")
print("==============================")
input("Please ask the mighty 8 ball your question:")
print("Please wait while the 8 ball works its magic...")
print("...")
print("...")
# i = random.randint(0, len(responses)-1) # TODO replace with random number
# print(f"The magic 8 ball says: {responses[i]}")
random.shuffle(responses)
print(f"The magic 8 ball says: {responses[0]}")





