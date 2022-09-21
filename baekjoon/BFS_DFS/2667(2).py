
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    ans = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                ans += 1
                queue.append((nx, ny))

    return ans


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
count = 0
res = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            count += 1
            res.append(bfs(i, j))

res.sort()
print(len(res))
[print(i) for i in res]