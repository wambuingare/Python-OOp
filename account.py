class Account:
    def __init__(self,account_name,account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []


    def deposit(self,amount):
        self.deposits.append(amount)
        if amount <= 0:
           return f"Deposit must be positive amount"
        else:
            self.balance += amount
            return f"Hello {self.account_name} you have deposited {amount} and your balance is {self.balance} your deposit statement is {self.deposits}"
    
      
    def withdraw(self,amount):
        self.transaction = 100
        if amount>self.balance:
         return f"Your balance is {self.balance},you can't withdraw {amount}"
        elif amount<0:
         return f"Withdrawal must be positive"
        else:
            self.balance -= amount+self.transaction
            self.withdrawals.append(amount)
            return f"Hello {self.account_name} you have withdrawn {amount} and your new balance is {self.balance} your withdrawal statement is {self.withdrawals}"


    def deposit_statement(self):
        for z in self.deposits:
         print(z,end="\n")

    def withdrawal_statement(self):
        for w in self.withdrawals:
         print(w,end="\n")

    def current_balance(self):
        return self.balance
            

     
            
    

     
        

