class Account:
    def __init__(self,account_name,account_number,balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance


    def deposit(self,amount):
        self.balance+=amount
        return self.balance

    def withdraw(self,amount):
        self.balance-=amount
        return self.balance
        