h, m = map(int, input().split())
time = int(input())

m += time

while m >= 60:
    if h == 23:
        h = 0
    else:
        h += 1
    m -= 60

print(h, m)