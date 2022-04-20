n, m = map(int, input().split())
arr = list(map(int, input().split()))

res = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            sum3Cars = arr[i] + arr[j] + arr[k]
            if sum3Cars <= m:
                res = max(res, sum3Cars)

print(res)
