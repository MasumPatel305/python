from datetime import datetime, timedelta

today = datetime.today()

thirty_days_ago = today - timedelta(days=30)

print("Today's Date:", today.strftime("%Y-%m-%d"))
print("30 Days Ago:", thirty_days_ago.strftime("%Y-%m-%d"))
