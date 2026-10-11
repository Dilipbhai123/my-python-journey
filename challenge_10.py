user_marks = {"Rajesh": 85, "Priya": 72, "Amit": 55}
grade = {}

for name, score in user_marks.items():
    if score >= 80:
        grade[name] = 'A'
    elif score >= 60:
        grade[name] = 'B'
    else:
        grade[name]= 'C'

print("your Result Is", grade)