import sys
inpyt = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
res = 0

while start < n:
    total = sum(arr[start:end + 1])

    if total == m:
        res += 1
        
    if total <= m:
        end += 1
        if end >= n:
            break
    else:
        start += 1

print(res)
