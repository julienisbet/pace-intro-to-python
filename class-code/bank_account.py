class BankAccount():
  def __init__(self, opening_balance):
    self.opening_balance = opening_balance
    self.balance = opening_balance
    self.transactions = []

  def __str__(self):
    return f"Current Balance: {self.balance}"

  def deposit(self, amount, type="DEPOSIT"):
    self.balance += amount
    self.transactions.append({
        'type': type,
        'amount': amount
      })

  def withdraw(self, amount, type="WITHDRAW"):
    if self.balance >= amount:
      self.balance -= amount
      self.transactions.append({
        'type': type,
        'amount': amount * -1
      })
    else:
      print("I'm sorry - you have insufficient funds")

  def transfer_to(self, transfer_account, amount):
    if self.balance >= amount:
      transfer_account.deposit(amount, type="TRANSFER")
      self.withdraw(amount, type="TRANSFER")
    else:
      print("I'm sorry - you have insufficient funds")

  def print_transactions(self):
    print("Here is a list of your transactions:")
    i = 0
    for t in self.transactions:
      print(f"\t{i}: {t['type']} for ${t['amount']}")
      i += 1


a = BankAccount(1000)
b = BankAccount(2000)
a.deposit(100)
a.transfer_to(b, 200)
a.print_transactions()
a.transfer_to(b, 100)
print(a.balance)
print(a.transactions)
print(b.balance)
b.deposit(200)
print(b.transactions)
print(b.balance)

b = BankAccount(100)
b.deposit(200)
print(b.balance)
print(b.transactions)
b.withdraw(100)
print(b.balance)
b.withdraw(300)











