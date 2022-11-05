import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

res = sys.maxsize
summary = 0
end = 0

for start in range(n):

    while summary < m and end < n:
        summary += arr[end]
        end += 1

    if summary == m:
        res = min(res, end - start)

    summary -= arr[start]

print(res)