arr = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FIR', 'SAT']
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0

m, d = map(int, input().split())

for i in range(m - 1):
    days += months[i]

print(arr[(days + d) % 7])