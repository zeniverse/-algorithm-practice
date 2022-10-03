
from collections import deque


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False] * m for _ in range(n)]

def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    visited[x][y] = True
    arr[x][y] = 1
    size = 2

    while queue:
        x_, y_ = queue.popleft()

        for i in range(4):
            nx = x_ + dx[i]
            ny = y_ + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                arr[nx][ny] = size
                size += 1
                queue.append((nx, ny))


count = 0

for i in range(n):
    for j in range(m):
        if arr[i][j ] == 1 and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)
print(max([max(i) for i in arr]))