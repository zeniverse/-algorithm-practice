import sys
input = sys.stdin.readline

n = int(input())

start = 1
end = n
res = 0

while start <= end:
    mid = (start + end) // 2

    if mid ** 2 >= n:
        res = mid
        end = mid - 1
    else:
        start = mid + 1

print(res)