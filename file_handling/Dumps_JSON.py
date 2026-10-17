import json

data = {"name": "rahul", "S_Id": "E1", "City": "B.K", "Studen_is": "True"}

student = json.dumps(data, indent=2)
print(student)