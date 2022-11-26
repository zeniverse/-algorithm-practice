n = int(input())
count = 0

for _ in range(n):
    day = int(input()[2:])
    
    if day <= 90:
        count += 1

print(count)