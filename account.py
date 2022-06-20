
from datetime import datetime


class Account:
    def __init__(self,account_name,account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.Id = id
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.transaction=100
        self.loan_balance=0
        self.date=datetime.now().strftime("%x %X")
       

    def deposit(self,amount):
        date=datetime.now()
        self.amount=amount 
        if amount<=0:
           return f"Dear customer,your deposit amount must be greater than 0"
        else:
            self.balance += amount
            dct={"date":date.strftime("%d/%m/%Y"),"amount":amount,"narration":f'Thank you for depositing Ksh.{amount} on {date}'}

            self.deposits.append(dct)
        return f"Dear customer,you have deposited Ksh.{amount} and your new balance is {self.balance})"
           
      
    def withdraw(self,amount):
        self.amount=amount
        date=datetime.now()
        if amount>self.balance:
         return f"Dear customer,you have insuffient funds in your accounts for you to withdraw."
        elif amount<=0:
          return f"Dear Customer,you can't withdraw amount less than 0"
        else:
            self.balance -=amount
            dct={"date":date.strftime("%d/%m/%Y"),"amount":amount,"narration":f'Thank you for withdrawing {amount} on {date}'}
            self.withdrawals.append(dct)
            withdrawal_amount=self.balance-self.transaction
        if amount>withdrawal_amount:
         return f"Dear Customer,you have insufficient balance."
        self.balance-=amount+self.transaction
        return f"{self.account_name} Confirmed you have withdrawn Ksh.{amount} and your new balance is {self.balance} on {date.strftime('%d/%m/%Y')})"


    def deposit_statement(self):
        for z in self.deposits:
            print(z)

    def withdrawal_statement(self):
         for w in self.withdrawals:
             print(w)

    def current_balance(self):
       return f"Dear customer,your current balance is Ksh.{self.balance}"

    def full_statement(self):
        statement=self.deposit+self.withdrawals
        for z in statement:
           print(z["narration"])
    def borrow(self,amount):
       sum=0
       for w in self.deposits:
           sum+=["amount"]
           
           if len(self.deposits) <10:
            return f"Dear customer you are not allowed to borrow.{10- len(self.deposits)} to borrow"
           if amount<100:
            return f"Dear customer you are allowed to borrow atleast 100"
           if amount>sum/3:
             return f"Dear customer,you can only borrow upto {sum/3}"
           if self.balance !=0:
            return f"Dear customer,you have Ksh.{self.balance},you can't borrow while still you have balance on your account."
           if self.loan_balance !=0:
            return f"Dear customer,you have a debt of Ksh.{self.loan_balance}pay the outstanding balance for you to get another loan."
       else:
        interest = 3/100*(amount)
        self.loan_balance+=amount+interest
        return f"Dear customer, you have borrowed a loan of Ksh.{amount},and your current loan is Ksh.{self.loan_balance}"

    def loan_repayment(self,amount):

        if amount>self.loan_balance:
           self.balance+=amount-self.loan_balance
           self.loan_balance=0
           return f"Dear customer,thank you for paying the outstanding loan of Ksh.{amount-self.loan_balance} and your account balance is Ksh.{self.balance}"
        else:
              self.loan_balance-=amount
              return f"Thank you."

    def transfer(self,amount,new_account):
        if amount<=0:
           return "invalid amount"
        if amount>=self.balance:
           return f"Dear customer,you have insufficient funds to transfer money from your account."
        if isinstance(new_account,Account):
           self.balance-=amount
        new_account.balance+=amount
        return f"You have successfully sent Ksh.{amount} to {new.account.name} account {new_account}.Your new balance is {self.balance}"    
                    
            

          
            

     
            
    

     
        

