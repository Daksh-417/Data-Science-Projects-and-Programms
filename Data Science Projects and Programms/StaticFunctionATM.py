class ATM:
    def __init__(self, balance):
        self.balance = balance
    def check_balance(self):
        print("Balance: ₹", self.balance)
    def deposit(self):
        a = int(input("Enter amount to deposit: ₹"))
        self.balance += a
        print("Deposited ₹", self.balance)
    def withdraw(self):
        a = int(input("Enter amount to withdraw: ₹"))
        if a <= self.balance:
            self.balance -= a
            print("Withdrawn ₹", a)
        else:
            print("Not enough balance!")
    def atm(self):
        while True:
            print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("Thank you! Visit again.")
                break
            else:
                print("Invalid option.")
atm_obj = ATM(balance=10000)
atm_obj.atm()
