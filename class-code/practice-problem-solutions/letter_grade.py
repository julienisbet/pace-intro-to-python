def letter_grade(num_grade):
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
print(letter_grade(100))
print(letter_grade(89))
print(letter_grade(82))
print(letter_grade(75))
print(letter_grade(68))
print(letter_grade(55))