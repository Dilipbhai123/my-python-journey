import csv

try:
    data = [
        ["નામ", "રોલ ન", "કોર્સે"],
        ["રાહુલ", "101", "પયથોન"],
        ["નેહા", "102", "જાવા"],
        ["સૂર્યા", "103", "c++"]
    ]
    with open("file/Student.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("ફાઇલ સફળતાપૂર્વક બની ગઈ છે")

except FileNotFoundError:
    print("મફકરસો ફાઇલ મળી નથી")

except Exception as e:
    print(f"કોઈ અજ્ઞાત ભૂલ આવી {e}")