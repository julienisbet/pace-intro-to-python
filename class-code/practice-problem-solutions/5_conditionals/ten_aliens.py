aliens = ['red', 'green', 'blue', 'green', 'blue', 'red', 'green', 'green', 'blue', 'red']
current_score = 0
for alien in aliens:
  if alien == 'red':
    current_score += 5
  elif alien == 'green':
    current_score += 10
  elif alien == 'blue':
    current_score += 20

print(current_score)

reds = aliens.count('red')
greens = aliens.count('green')
blues = aliens.count('blues')

print(reds*5 + greens * 10 + blues*20)

