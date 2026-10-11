principal = float(input("Entar Your Amount :"))
rate = float(input("Entar Your rate :"))
time = float(input("Entar Your time month :"))
SI = (principal * rate * time) / 100

print("your intrest is {} and Your Total is {}" .format(SI, principal+SI))