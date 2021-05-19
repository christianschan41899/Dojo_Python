class User:
    def __init__(self, name, email_address):
        self.name = name			
        self.email = email_address		
        self.account_balance = 0

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_balance(self):
        print(self.account_balance)

    def transfer_money(self, user, amount):
        self.make_withdrawl(amount)
        user.make_deposit(amount)

user1 = User("Dan", "dan@email.com")
user2 = User("Lili", "li@mail.com")
user3 = User("Dude", "temp@gmail.com")

user1.make_deposit(40).make_deposit(200).make_deposit(50)
print("User Dan made 3 deposits")

user1.make_withdrawl(60)
print("User Dan made a withdrawl")

print("User Dan's account balance is:")
user1.display_balance()

user2.make_deposit(1200).make_deposit(140)
print("User Lili made 2 deposits")

user2.make_withdrawl(1000).make_withdrawl(100)
print("User Lili made 2 withdrawls")

print("User Lili's account balance is:")
user2.display_balance()

user3.make_deposit(1200)
print("User Dude made a deposit")

user3.make_withdrawl(1000).make_withdrawl(100).make_withdrawl(300)
print("User Dude made 3 withdrawls")

print("User Dude's account balance is:")
user3.display_balance()

user1.transfer_money(user3, 200)
print("Dan transfered money to Dude")
print("Dan's balance is:")
user1.display_balance()
print("Dude's balance is:")
user3.display_balance()
