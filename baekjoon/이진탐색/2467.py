
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

start = 0
end = n - 1
res = [0, 0]
_min = sys.maxsize

while start < end:
    total = arr[start] + arr[end]

    if abs(total) < _min:
        res[0] = arr[start]
        res[1] = arr[end]
        _min = abs(total)


    if total < 0:
        start += 1
    elif total > 0:
        end -= 1
    else:
        break

print(*res)
