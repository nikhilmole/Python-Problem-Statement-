class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = '\0'
        self.Amount = 0
        self.withdraw = 0
        self.remaining = 0
        self.interest = 0
        print("Name account holder:")
        self.Name = str(input())
    
    def Deposit(self):
        print("Enter amount you want to add in account:")
        self.Amount = int(input())

    def Withdraw(self): 
        print("Enter amount you want to withdraw:")
        self.withdraw = int(input())
        self.remaining = self.Amount - self.withdraw
        print("Remaining balance is:", self.remaining)

    def CalculateInterest(self):
        self.interest = self.Amount * BankAccount.ROI / 100
        print("Interest calculated on the current balance:", self.interest) 

    def Display(self):
        print("Account holder name:", self.Name)
        print("Current Balance is:", self.Amount)

def main():
    obj1 = BankAccount()

    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateInterest()
    obj1.Display()

if __name__ == "__main__":
    main()
