from savings_account import SavingsAccount, SavingsAccountfrom 
from checking_account import CheckingAccount, CheckingAmmount

def main():
    print("Welcome to the Bank Account Mannagement System!")
    
    account_holder = input("enter your name: ")
    account_type = input("choose account type(savings/checking): ").lower()
    
    if account_type == "savings":
        account = SavingsAccount(account_holder)
    elif account_type == "checking":
        account = CheckingAccount(account_holder)
    else:
        print("Invalid account type.")
        return
    
    while True:
        print("\n==== sampath bank ====")
        print("Account Menu:")
        print("options:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter the deposite ammount"))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("enter the withdrawal amount"))
            account.withdraw(amount)
        elif choice == "3" :
            print(f"Account Balance: {account.get_balancce()}")
        elif choice == "4":
            print("exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice.Please try again.")
            
if __name__ == "__main__" :
    main()
            
        