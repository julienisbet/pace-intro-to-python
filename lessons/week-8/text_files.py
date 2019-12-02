# filename = 'pi_digits.txt'
# with open(filename) as f:
#   for line in f:
#     print(line.rstrip())

# pi_string = ''
# with open(filename) as f:
#   for line in f:
#     pi_string += line.strip()

# print(pi_string)

filename = 'pi_million_digits.txt'
pi_string = ''
with open(filename) as f:
  for line in f:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
  print ("Your birthday appears in the first million digits of pi")
else:
  print("Bummer, your birthday isn't in the first million digits of pi")


# do is birthday contained in python exercise