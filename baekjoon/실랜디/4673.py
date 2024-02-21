arr = set(range(1, 10001))
selfNumber = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    selfNumber.add(i)

for i in sorted(arr - selfNumber):
    print(i)