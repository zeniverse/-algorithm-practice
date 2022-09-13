import sys
input = sys.stdin.readline

s = int(input())
res = 0

start =1
end = s

while start <= end:
    mid = (start + end) // 2

    if mid * (mid + 1) // 2 <= s:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)