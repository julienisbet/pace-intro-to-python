class Dog():
  '''A class for representing dogs'''
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  # every method call associated with an instance automatically passes self
  # self is a reference to the instance itself
  def bark(self):
    print(f"{self.name} says bark bark!")

benny = Dog("Benny", "Terrier Mix", 4)

print(benny.name)
benny.bark()