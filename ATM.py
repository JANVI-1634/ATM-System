#ATM Software

class ATM:
    def __init__(self,balance):
        self.balance=balance

    def check_balance(self):
        print("Current Balance:",self.balance)

    def deposit(self):
        amount=float(input("Enter Amount:"))
        if amount > 0:
            self.balance+=amount
            print("Deposited Amount:",amount)
            print("New Balance:",self.balance)
        else:
            print("Invaild amount...")
    
    def withdraw(self):
        amount=float(input("Enter Amount:"))
        if amount > self.balance:
            print("Insufficient Amount")
        elif amount <= 0:
            print("Invalid amount")
        else:
            self.balance-=amount
            print("Withdrawal Amount:",amount)
            print("New Balance",self.balance)
#-------Main Program--------
PIN=input("Enter PIN:")

atm =ATM(10000) 
 
while True:
    if PIN == "Janvi":
        print("what you want to do:")
        print("1.Check Balance")
        print("2.deposit Money")
        print("3.Withdraw Money")
        print("4. Exit")
    else:
        print("Wrong PIN...Please try again")
    choice = input("Enter you choice 1,2,3,4:")


    if choice == "1":
        atm.check_balance()
    elif choice == "2":
        atm.deposit()
    elif choice == "3":
        atm.withdraw()
    elif choice == "4":
        print("\nThank you for using our ATM.")
        exit()
else:
    print("Your choice is incorrect")
