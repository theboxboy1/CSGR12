class ATM:
    
    def __init__(self, balance = 0, pin =None):
        self.balance = balance
        
        if pin is not None:
            self.pin = pin
        else:
            self.pin = input("Create a pin: ")
        
        if not self.pin:
            print("PIN not set")

        else:
            print("PIN set")
       
        
        
    def withdraw(self,amount):
        
        self.balance -= amount
    
        
        print(f"You withdrew: ${amount}\nYour current balance is: ${self.balance}")
        
        
    
    def deposit(self,money_in):

        self.balance += money_in
        print(f"You deposited: ${money_in}\nYour current balance is: ${self.balance}")
            
    def total_balance(self):
        
        print(f"Your balance is: ${self.balance}")


