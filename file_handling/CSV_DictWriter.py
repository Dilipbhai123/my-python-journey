import csv

data = [
    {"ID": "E1", "NAME": "Rahul", "CITY": "Ahmedabad", "SALARY": "50000"},
    {"ID": "E2", "NAME": "Rohan", "CITY": "Gandhinagar", "SALARY": "60000"},
    {"ID": "E3", "NAME": "Rosani", "CITY": "Gandhinagar", "SALARY": "55000"},
    {"ID": "E4", "NAME": "Jyosna", "CITY": "B.K", "SALARY": "66000"}
]

header = ["ID", "NAME", "CITY", "SALARY"]

with open("file/Employ.csv", "w", newline="", encoding="utf-8")as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)
print("Data Created Sucsessfull")