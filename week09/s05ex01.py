from datetime import datetime, timedelta

today = datetime.today()
dates = [today - timedelta(days=3 * i) for i in range(5)]

sorted_dates = sorted(dates)

formatted_dates = [date.strftime("%Y-%m-%d") for date in sorted_dates]
print(formatted_dates)
