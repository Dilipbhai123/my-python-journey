# membership oprators is  ( in , not in)

print("D" in "Dilip")
print("d" in "Dilip")
print("p" in "python")
print("j" in "python")
print("t" in "python")


password = input("Entar Your password:")

if "@" in password and len(password) >= 8:
    print("strong")
else:
    print("weak")
