name = input("entar your name:")
ganit = float(input("entar your maths percentage:"))
sciece = float(input("entar your science percentage:"))
english = float(input("entar your english percentage:"))
gujrati = float(input("entar your gujrati percentage:"))
hindi = float(input("entar your hindi percentage:"))

total = ganit + sciece + english + gujrati + hindi

percentage = total / 5


print("=" * 35)
print("              Riport Card is               ")
print("=" * 35)
print(f"name :        {name}")
print(f"maths =       {ganit} science = {sciece} english = {english} gujrati = {gujrati} hindi = {hindi}")
print(f"total is      {total}")
print(f"percentage is {percentage}")
print("=" * 35)