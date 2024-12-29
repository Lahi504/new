from bank_account import BankAccount

#Derived class SavingAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super()._imit_(account_holder, balance)
        self.interest_rate = interest_rate #public attribute

def add_interest(self):
    interest = self.balance * self.interest_rate
    self.balance += interest
    print(f"Added interest {self.interest_rate}. New balance: {self.balance}")