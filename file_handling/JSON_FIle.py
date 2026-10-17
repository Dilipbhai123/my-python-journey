import json

data = {
    "Nane": "Rohan",
    "Age": "22",
    "City": "B.K",
    "Is_Student": "True",
    "Student_Id": "E1",
    "Course": ['python','java', 'c++']
}

with open("file/Studen.json", "w", encoding="utf-8") as file:
    student_record = json.dump(data, file, indent=4, ensure_ascii=False)
print("file Created Succsessfull")