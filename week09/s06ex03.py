import csv
from datetime import datetime

tasks = [
    {"task": "Finish report", "deadline": "2025-10-10"},
    {"task": "Attend meeting", "deadline": "2025-09-28"},
    {"task": "Submit project", "deadline": "2025-10-01"},
    {"task": "Review code", "deadline": "2025-09-25"},
    {"task": "Update website", "deadline": "2025-10-05"}
]

with open('tasks.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["task", "deadline"])
    writer.writeheader()
    writer.writerows(tasks)

with open('tasks.csv', mode='r') as file:
    reader = csv.DictReader(file)
    task_data = list(reader)

sorted_tasks = sorted(task_data, key=lambda x: datetime.strptime(x["deadline"], "%Y-%m-%d"))

for task in sorted_tasks:
    print(f"{task['task']} (Deadline: {task['deadline']})")
