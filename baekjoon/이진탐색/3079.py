
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = []

for _ in range(n):
    times.append(int(input()))

times.sort()

start = 1
end = m * max(times)
res = 0

while start <= end:
    mid = (start + end) // 2

    total = sum([mid // time for time in times])

    if total >= m:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)


