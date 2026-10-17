import csv

with open("file/Student.csv", "r", newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Student Name Is {row['નામ']} and Rol Number {row['રોલ ન']} and course {row['કોર્સે']}")