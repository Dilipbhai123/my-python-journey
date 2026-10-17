import csv

account_num = "1234567890"

user_name = input("Entar Your AS Par Adhar Name :")
user_adhar = int(input("Entar Your 12 Digit Adhar Num :"))
user_pan = input("Entar Your PAN Number :")

class BankAcount:
    def __init__(self, name, adhar, pan):
        self.name = name
        self.__adhar = adhar
        self.__pan = pan

    @property
    def adhar(self):
        return self.__adhar

    @property
    def pan(self):
        return self.__pan

    def create_ac_file(self):
            adhar = str(self.__adhar)
            myacc = account_num + adhar[-4:]
            data = [
                ["name", "adhar", "pan", "ac"],
                [self.name, self.__adhar, self.__pan, myacc]
            ]
            with open("file/BankFast.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(data)
                print("Your Account Created Sucsessfull")
            print(f"Your AC Number For : {myacc}")

myobb = BankAcount(user_name, user_adhar, user_pan)

myobb.create_ac_file()