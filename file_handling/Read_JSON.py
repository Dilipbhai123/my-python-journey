import json

with open("file/Studen.json", "r", encoding="utf-8") as file:
    student = json.load(file)
    print(student)