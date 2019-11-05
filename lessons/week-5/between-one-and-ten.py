import random
guessed_correctly = False
my_num = random.randint(1, 10)
while guessed_correctly == False:
  guess = int(input("Please guess a number between one and ten: "))
  if guess == my_num:
    print("You guessed guessed_correctly!")
    guessed_correctly = True
  elif guess > my_num:
    print("No dice -- try a lower number!")
  else:
    print("No dice -- try a higher number!")
