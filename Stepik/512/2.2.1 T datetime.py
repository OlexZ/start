from datetime import datetime, timedelta

time = datetime.strptime(input(), '%Y %m %d')
days = timedelta(int(input()))
time = (time + days)
print(time.year, time.month, time.day)