from bank_account import BankAccount

#Derived clss CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=500):
        super()._init_(account_holder, balance)
        self.overdraft_limit = overdraft_limit
        
    def withdraw(self, amount):
        if amount > 0 and amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
            print(f"Overdraft limit: {self.overdraft_limit}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")