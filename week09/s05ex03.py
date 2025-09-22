from datetime import datetime, timedelta

today = datetime.today()
due_date = today + timedelta(days=14)
print("Due Date (14 days from today):", due_date.strftime("%Y-%m-%d"))
