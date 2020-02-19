# This is our code from earlier in the class
# that converts number grades to letter grades
# Its currently working for the first example
# but the second example 75 is also printing A
# Can you spot the problem?

def letter_grade(num_grade):
  num_grade = 93
  if num_grade >= 90:
    grade = 'A'
  elif num_grade >= 80:
    grade = 'B'
  elif num_grade >= 70:
    grade = 'C'
  elif num_grade >= 60:
    grade = 'D'
  else:
    grade = 'F'

  if grade != 'F':
    minus_plus = num_grade % 10
    if minus_plus >= 7 or num_grade == 100:
      grade = grade + "+"
    elif minus_plus <=2:
      grade = grade + '-'

  return grade

print(letter_grade(93))
print(letter_grade(75))