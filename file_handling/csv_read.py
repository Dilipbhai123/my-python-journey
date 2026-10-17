import csv

try:
    with open("file/Student.csv", "r", newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("file is Not Found")

except Exception as e:
    print(f"faind annon error {e}")
