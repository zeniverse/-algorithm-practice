
from collections import deque
import sys

input = sys.stdin.readline


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()
res = -1

visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append((i, j))

while queue:
    for _ in range(len(queue)):
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and arr[nx][ny] == 0:
                visited[nx][ny] = True
                arr[nx][ny] = 2
                queue.append((nx, ny))

    res += 1

flag = False

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            flag = True
            break

if flag:
    print(-1)
else:
    print(res)
        

