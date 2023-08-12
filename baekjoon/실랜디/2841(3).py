from collections import deque
import sys
input = sys.stdin.readline

n, p = map(int, input().split())
arr = [deque([]) for _ in range(7)]
res = 0

for _ in range(n):
    line, num = map(int, input().split())

    if not arr[line]:
        arr[line].appendleft(num)
        res += 1
    else:
        while arr[line] and arr[line][0] > num:
            arr[line].popleft()
            res += 1
        if not arr[line] or arr[line][0] != num:
            arr[line].appendleft(num)
            res += 1
print(res)