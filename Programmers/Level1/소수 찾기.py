import math

n = 10

arr = [True] * (n + 1)
count = 0

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        for j in range(i + i, n + 1, i):
            arr[j] = False

for i in range(2, n + 1):
    if arr[i]:
        count += 1

print(count)

