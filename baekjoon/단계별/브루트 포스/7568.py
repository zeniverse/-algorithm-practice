n = int(input())
arr = []
res = [1] * n

for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

for i in range(n):
    for j in range(n):
        if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            res[j] += 1

print(*res)



