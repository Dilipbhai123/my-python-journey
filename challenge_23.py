class DigitalWallet:
    def __init__(self, user_name, balance):
        self.user_name = user_name
        self.__balance = balance

    @property
    def balance(self):
        print("[LOG]: Balance જોવાની પ્રોસેસ થઈ રહી છે")
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("❌ ભૂલ: ખોટી વેલ્યૂ એન્ટર કરી છે (માઇનસમાં રકમ ન ચાલે).")            
            return
        
        if self.__balance + amount <= 10000:
            self.__balance += amount
            print("તમારૂ અમાઉન્ટ સફળતા પૂર્વક એડ કરી દેવામાં આવ્યું", amount)
        elif self.__balance + amount > 10000:
            print("અમાઉન્ટ રકમ ૧૦,૦૦૦ થી ઓછી હોવી જોઈએ")
        else:
            print("ખોટી વેલ્યૂ એન્ટર કરી છે ")

my_wall = DigitalWallet("Rahul", 1000)

print(my_wall.balance)

my_wall.balance = 5000
print(my_wall.balance)

my_wall._DigitalWallet__balance = 0
print(my_wall.balance)