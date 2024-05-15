n = int(input())
arr = list(map(int, input().split()))

res = [0] * n
min_ = arr[0]

for i in range(1, n):
    min_ = min(min_, arr[i])
    res[i] = max(res[i - 1], arr[i] - min_)

print(*res)