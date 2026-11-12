class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def display_balance(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

account = BankAccount("Kaveeta Kumari", 1000)

account.deposit(5000)
account.withdraw(1500)
account.display_balance()