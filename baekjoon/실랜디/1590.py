n, t = map(int, input().split())
res = []

for _ in range(n):
    s, i, c = map(int, input().split())
    time = [s + (i * c) for c in range(c)]

    if time[-1] < t:
        continue

    start = 0
    end = c - 1
    ans = 0

    while start <= end:
        mid = (start + end) // 2

        if time[mid] >= t:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    res.append(time[ans] - t)

if res:
    print(min(res))
else:
    print(-1)