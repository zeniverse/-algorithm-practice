import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
res = []

for i in range(n):
    for j in range(i+1, n):
        if arr[i] < arr[j]:
            res.append(arr[j])
            break
    else:
        res.append(-1)

print(*res)
