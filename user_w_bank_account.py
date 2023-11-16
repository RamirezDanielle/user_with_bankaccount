class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.user_account= BankAccount(int_rate=0.02, balance = 0)

    def make_deposit(self, amount):
        self.user_account.deposit(amount)

    def account_info(self):
        self.user_account.display_account_info(self.name)

    def make_withdrawal(self, amount):
        self.user_account.withdraw(amount)

    def yield_interest(self):
        self.user_account.yield_interest()

    def account(self):
        self.account.deposit(100)
        print(self.account.balance)


class BankAccount:
    def __init__(self, int_rate=0.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_account_info(self, user_name):
        print(f"{user_name}'s Account - Balance: {self.balance}")

    def yield_interest(self):
        self.balance += self.balance * self.int_rate

user1 = User("Bruce Waybe", "Brucewayne@roadrunner.com")
user1.make_deposit(500)
user1.account_info()
user1.make_withdrawal(200)
user1.account_info()
user1.yield_interest()
user1.account_info()