# Update the withdrawal method to store each withdrawal transaction as 
# a dictionary like like this
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }
# Update the deposit method to store each deposit transaction as a 
# dictionary like this
# {
#    "date": datetime object,
#    "amount": amount,
#    "narration": deposit or withdrawal
# }
# Add a new method  full_statement which combines both deposits and
#  withdrawals into one list ordered by date and using a for loop prints 
#  each transaction in a new line like this
# 16/06/22 —----- Deposit —---- 1000
# Add a new attribute loan_balance which is zero by default.
# Add a borrow method which allows a customer to borrow if they meet these 
# conditions:
# Customer has made at least 10 deposits.
# Loan amount requested must be more than 100
# A customer qualifies for a loan amount that is less than  or equal to 1/3 of 
# their total sum of deposit history
# Customer account has no has no balance
# Customer has no outstanding loan
# The loan attracts  an interest of 3%.
# Add a loan repayment method with these conditions
# A customer can repay a loan to reduce the current loan balance
# Overpayment of a loan increases a customers current deposit
# Add a new method transfer which accepts two attributes (amount and instance of 
# another account). If the amount is less than the current instances balance, the
#  method transfers the requested amount from the current account to the passed 
#  account. The transfer is accomplished by reducing the current account balance and 
#  depositing the requested amount to the passed account





class Student:
     school = "Akirachix"
     def __init__(self,country,firstname,secondname,age):
        self.firstname = firstname
        self.country = country
        self.secondname = secondname
        self.age = age
     def full_name (self):

         return f"Hello {self.firstname} {self.secondname} How is {self.country}"
     def year_of_birth (self):  
        year=2022 - self.age
        return f"Hello {self.firstname} {self.secondname} How is {self.country} you were born in {year}"
     def initials (self):
         return f"Hello {self.firstname} {self.secondname} How is {self.country} your initials are {self.firstname[0]} {self.secondname[0]}"