import datetime

n, m = map(int, input().split())
dic = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FIR', 5:'SAT', 6:'SUN'}
print(dic[datetime.datetime(2007, n, m).weekday()])