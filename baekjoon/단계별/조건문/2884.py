h, m = map(int, input().split())

if m >= 45:
    m -= 45
else:
    if h == 0:
        h = 23
    else:
        h -= 1
    
    m = 60 - (45-m)

print(h, m)
