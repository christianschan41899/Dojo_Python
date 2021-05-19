class User:
    def __init__(self, name, email_address):
        self.name = name			
        self.email = email_address		
        self.account = BankAccount(int_rate=0.04, balance=0)

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.bal += amount
        return self

    def make_withdrawl(self, amount):
        self.account.bal -= amount
        return self

    def display_balance(self):
        print(f"The balance of the account is currently {self.account.bal}")

    def transfer_money(self, user, amount):
        self.make_withdrawl(amount)
        user.make_deposit(amount)

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
	def yield_interest(self):
		if(self.bal>0):
		    self.bal += (self.bal*self.interest)
		return self


user1 = User("Dan", "dan@email.com")
user2 = User("Lili", "li@mail.com")
user3 = User("Dude", "temp@gmail.com")

user1.make_deposit(40).make_deposit(200).make_deposit(50).make_withdrawl(60)
print("User Dan made 3 deposits and a withdrawl")
user1.display_balance()

user2.make_deposit(1200).make_deposit(140).make_withdrawl(1000).make_withdrawl(100)
print("User Lili made 2 deposits and 2 withdrawls")
user2.display_balance()

user3.make_deposit(1200).make_withdrawl(1000).make_withdrawl(100).make_withdrawl(300)
print("User Dude made a deposit and 3 withdrawls")
user3.display_balance()

user1.transfer_money(user3, 200)
print("Dan transfered money to Dude")
print("For Dan...")
user1.display_balance()
print("For Dude...")
user3.display_balance()
