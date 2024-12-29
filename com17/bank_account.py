#Base class account
class BankAccount:
    def __init__(self,account_holder=None, balance=0):
        self.account_holder= account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("invalid deposit amount.")

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"WIthdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def get_balance(self):
        return self.balance