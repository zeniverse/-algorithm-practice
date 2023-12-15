n = int(input())
arr = [int(input()) for _ in range(n)]
arr = sorted(arr)

res = []

for i in range(0, n):
    count = 0
    for j in range(arr[i], arr[i] + 5):
        if j not in arr:
            count += 1
    res.append(count)

print(min(res))