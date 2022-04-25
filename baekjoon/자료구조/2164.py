from collections import deque
import sys

n = int(sys.stdin.readline())
arr = list(range(1, n + 1))
d = deque(arr)

while len(d) != 1:
    d.popleft()
    d.append(d[0])
    d.popleft()

print(*d)