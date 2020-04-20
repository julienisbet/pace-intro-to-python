def days_in_month(month, year=2020):
  if month == 2:
    if year % 4 == 0:
      return 29
    else:
      return 28
  elif month in(4,6,9,11):
    return 30
  else:
    return 31

for i in range(1, 13):
  print(days_in_month(i))

for i in range(1, 13):
  print(days_in_month(i, 2021))