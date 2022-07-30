import datetime

a = 5
b = 24

days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
print(days[datetime.date(2016, a, b).weekday()])