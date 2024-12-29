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
    
#Derived class SavingAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super()._imit_(account_holder, balance)
        self.interest_rate = interest_rate #public attribute

def add_interest(self):
    interest = self.balance * self.interest_rate
    self.balance += interest
    print(f"Added interest. New balance: {self.balance}")
    
#Derived clss CheckingAccount
class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=500):
        super()._init_(account_holder, balance)
        self.overdraft_limit = overdraft_limit
        
    def withdraw(self, amount):
        if amount > 0 and amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
            
        
#polymorphism example
def display_accont_info(account):
    print(f"Account Holder: {account.account_holder}")
    print(f"Balance: {account.get_balance()}")
        
        
#main program using polynorphism to create instrances of diffrent account types

def main():
    #create intances of different accont types
    print("==== Sampath Bank ====")
    saving_account = SavingsAccount("Chamal Kanchana", 1500)
    checking_account = CheckingAccount("Lahiru Sahan", 1000)
    
    print("\n[Savings Account opeerations]")
    saving_account.deposit(200)
    saving_account.add_interest()
    display_accont_info(SavingsAccount)
    
    print("\n[Checking Account opeerations]")
    checking_account.withdraw(800)
    checking_account.withdraw(800)
    display_accont_info(checking_account)
    
if __name__ == "_main_":
    main()
