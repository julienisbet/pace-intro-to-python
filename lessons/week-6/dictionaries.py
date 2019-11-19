my_pizza = {
  'crust': 'gluten_free',
  'cheese': 'light',
  'slices': 8,
  'toppings': ['pepperoni', 'musrooms']
}

print(my_pizza['crust'])
print(my_pizza['slices'])

a = 'crust'

print(my_pizza[a])

my_pizza['toppings'].append('pineapple')
print(my_pizza)

del my_pizza['crust']
print(my_pizza)

for key, value in my_pizza.items():
  print(key)
  print(value)

for key in my_pizza:
  print(key)
