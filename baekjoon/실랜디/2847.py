n = int(input())
arr = []
res = 0

for _ in range(n):
    arr.append(int(input()))

start = arr[-1]

for i in range(n - 2, -1, -1):
    while arr[i] >= start:
        res += 1
        arr[i] -= 1

    start = arr[i]

print(res)