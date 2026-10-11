student = int(input("entar your parsantage :"))

if student >= 0 and student <= 35:
    print("your grade is E")
elif student >= 36 and student <= 50:
    print("your grade is D")
elif student >= 51 and student <= 75:
    print("your grade is C")
elif student >= 76 and student <= 85:
    print("your grade is B")
elif student >= 86 and student <= 100:
    print("your grade is A")
else:
    print("your wrong persantage")