import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

res = 0

while start <= end:
    total = 0

    mid = (start + end) // 2

    for x in trees:
        if x > mid:
            total += x - mid

    if total < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1

print(res)
