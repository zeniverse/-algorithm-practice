
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())

start = 1
end = max(arr)

res = 0

while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in arr:
        total += min(x, mid)
    
    if total > m:
        end = mid - 1
    else:
        start = mid + 1

print(end)


    