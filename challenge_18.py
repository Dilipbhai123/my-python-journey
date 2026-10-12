'''Created a `BankAccount` class using classes and 
   objects that checks the account holder's name 
   and balance. '''

#BankAccount class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    #first method for chek account holder name
    def show_account(self):
        print(f"Account Holder Name Is : {self.account_holder}")

    #secound method for chek bank balance
    def show_balance(self):
        print(f"Your Balance Is : {self.balance}")

#Object
account_ball = BankAccount("Rahul Rayjada", 500000)

#user input for choice method
user = int(input("કઈ method call કરવી? (show_account press for 1 / show_balance press for 2): "))

#choice user method for coll method for if elif
if user == 1:
    account_ball.show_account()
elif user == 2:
    account_ball.show_balance()