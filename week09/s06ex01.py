# 1. Write student names/ages to CSV. Sort by age when reading.
import csv

students = [
    {"name": "Alice", "age": 22},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 23},
    {"name": "David", "age": 21}
]

with open('students.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(students)

with open('students.csv', mode='r') as file:
    reader = csv.DictReader(file)
    student_data = list(reader)

sorted_students = sorted(student_data, key=lambda x: int(x["age"]))

for student in sorted_students:
    print(f"{student['name']}: {student['age']}")
