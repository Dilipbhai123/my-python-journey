class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance if balance >= 0 else 0

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Your Deposit Amount Is : {amount}")
        else:
            print("Wrong Amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Your Withdrow Amount Is : {amount}")
        else:
            print("Insufistikated Amount")

abc = BankAccount("અમિત", 1000)
print("your total balanse is", abc.balance)

abc.deposit(500)
abc.withdraw(300)

print(f"your total balanse is {abc.balance}")