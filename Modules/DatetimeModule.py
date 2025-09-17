import datetime

d = datetime.date(2016, 7, 24)
print(d)

today = datetime.date.today()
print(today)

print(today.weekday())
print(today.isoweekday())

tdelta = datetime.timedelta(days = 7)

print(today + tdelta)

