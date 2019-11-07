

def count_larger_than_ten(numbers, gt=10):
  count_so_far = 0

  for number in numbers:
    if number > gt:
      count_so_far = count_so_far + 1

  return count_so_far

x = int(input("what number do you wanna check?"))
pile = [2, 14, 37, 1, 9, 15]
pile2 = [12, 14, 7, 11, 90, 15]
print(count_larger_than_ten(pile, x))
print(count_larger_than_ten(pile2, x))




