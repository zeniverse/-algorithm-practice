
from collections import deque
import sys
input = sys.stdin.readline

n, t = map(int, input().split())
dots = set()

for _ in range(n):
    a, b = map(int, input().split())
    dots.add((a, b))

queue = deque()
queue.append((0, 0, 0))

while queue:
    x, y, count = queue.popleft()

    if y == t:
        print(count)
        break

    for i in range(-2, 3):
        for j in range(-2, 3):
            nx = x + i
            ny = y + j

            if (nx, ny) in dots:
                queue.append((nx, ny, count + 1))
                dots.remove((nx, ny))
else:
    print(-1)


