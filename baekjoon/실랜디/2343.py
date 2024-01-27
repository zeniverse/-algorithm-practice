
n, m = map(int, input().split())
arr = list(map(int, input().split()))
res = 0

start = max(arr)
end = sum(arr)

while start <= end:
    mid = (start + end) // 2

    total = 0
    count = 1

    for i in arr:
        if total + i > mid:
            count += 1
            total = 0
        total += i

    if count <= m:
        res = mid
        end = mid - 1

    else:
        start = mid + 1

print(res)