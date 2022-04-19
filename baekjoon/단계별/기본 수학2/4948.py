import math, sys

arr = [True] * 246913
prime_num = []

for i in range(2, int(math.sqrt(123456 * 2)) + 1):
    if arr[i]:
        for j in range(i + i, (123456 * 2) + 1, i):
            arr[j] = False

for i in range(2, (123456*2) + 1):
    if arr[i]:
        prime_num.append(i)

while True:
    n = int(sys.stdin.readline())
    count = 0

    if n == 0:
        break

    for i in prime_num:
        if i > n and i <= 2*n:
            count += 1

    print(count)
