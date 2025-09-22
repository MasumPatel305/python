# 2. Add a Registered On date for each student row.
import csv
from datetime import datetime

students = [
    {"name": "Alice", "age": 22, "registered_on": datetime.today().strftime("%Y-%m-%d")},
    {"name": "Bob", "age": 20, "registered_on": datetime.today().strftime("%Y-%m-%d")},
    {"name": "Charlie", "age": 23, "registered_on": datetime.today().strftime("%Y-%m-%d")},
    {"name": "David", "age": 21, "registered_on": datetime.today().strftime("%Y-%m-%d")}
]

with open('students.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "registered_on"])
    writer.writeheader()
    writer.writerows(students)

with open('students.csv', mode='r') as file:
    reader = csv.DictReader(file)
    student_data = list(reader)

sorted_students = sorted(student_data, key=lambda x: int(x["age"]))

for student in sorted_students:
    if student['name'] == "Charlie":
        student['registered_on'] = "2025-09-18"
    print(f"{student['name']}: {student['age']} (Registered On: {student['registered_on']})")


with open('students.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "registered_on"])
    writer.writeheader()
    writer.writerows(sorted_students)