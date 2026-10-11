balanse = 50000

def bank_balesh(balanse):
    print(f"Your Bank Balanse Is : {balanse}")

def withdrow_amount(amount):
    global balanse
    amo = balanse - amount
    balanse = amo
    print(f"Your Avelabel Amount IS : {amo}")

def add_amount(add):
    global balanse
    ad = balanse + add
    balanse = ad
    print(f"your Balanse Add Sucsesfull : {ad}")


while True:
    print(f"{'=' * 40}")
    print("            * Fata Fat Bank *")
    print(f"{'=' * 40}")
    print("1 : chek bank balanse")
    print("2 : Add Amount")
    print("3 : Withdrow Amount")
    print("4 : Quit for Fata Fat Bank")
    print(f"{'=' * 40}")

    choice = int(input("Entar Your Number :"))

    if choice == 1:
        pin = int(input("Entar Your Pin :"))
        if pin == 1234:
            bank_balesh(balanse)
    elif choice == 2:
        add = float(input("Entar Your add amount :"))
        add_amount(add)
    elif choice == 3:
        amount = float(input("Entar Your widrow amount :"))
        withdrow_amount(amount)
    elif choice == 4:
        print("Good By for Fata Fat Bank")
        break