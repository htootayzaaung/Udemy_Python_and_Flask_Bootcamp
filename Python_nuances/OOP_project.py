class Account:

	def __init__(self, owner, balance = 0):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return f"Account Owner: {self.owner}, Balance: {self.balance}"

	def deposit(self, dep_amt):
		self.balance += dep_amt
		print("Deposit was accepted!")

	def withdrawal(self, withdrawal_amt):
		if (self.balance > withdrawal_amt):
			self.balance -= withdrawal_amt
			print("Withdrawal successful")

		else:
			print("Funds not available!")


acc1 = Account("Jose", 100)

print(acc1)
print(acc1.owner)
print(acc1.balance)
acc1.deposit(250)
print(acc1.balance)
acc1.withdrawal(400)
