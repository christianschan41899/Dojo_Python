class BankAccount:
	def __init__(self, int_rate = 1, balance = 0):
		self.interest = (int_rate/100)
		self.bal = balance
	def deposit(self, amount):
		self.bal += amount
		return self
	def withdraw(self, amount):
		self.bal -= amount
		return self
	def display_account_info(self):
		print(f"The balance of the account is: {self.bal}")
	def yield_interest(self):
		if(self.bal>0):
		    self.bal += (self.bal*self.interest)
		return self

account1 = BankAccount(0.04, 500)
account2 = BankAccount(0.05, 700)

print("Account1 made 3 deposits and a withdrawl before they accrued interest")
account1.deposit(400).deposit(700).deposit(50).withdraw(300).yield_interest().display_account_info()

print("Account2 made 1 deposit and 3 withdrawls before they accrued interest")
account2.deposit(1000).withdraw(300).withdraw(400).withdraw(200).yield_interest().display_account_info()