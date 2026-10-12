#In the 'Mobile' class, class variables, methods, etc., are called.

class Mobile:
    opreting_system = "Android"

    def __init__(self, mobile_name, price):
        self.mobile_name = mobile_name
        self.price = price

    def show_detaild(self):
        print(f"{self.opreting_system} : {self.mobile_name} - ₹{self.price}")

samsung = Mobile("Samsung Galaxy A36 5G", 25999)
redmi = Mobile("REDMI Note 15 SE 5G Snapdragon", 25999)

samsung.show_detaild()