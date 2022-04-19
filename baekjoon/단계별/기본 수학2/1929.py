import sys, math

m, n = map(int, sys.stdin.readline().split())
arr = [True] * (n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        for j in range(i + i, n + 1, i):
            arr[j] = False

for i in range(m, n + 1):
    if i > 1 and arr[i]:
        print(i)