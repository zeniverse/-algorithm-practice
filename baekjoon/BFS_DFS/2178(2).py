
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        if x == n - 1 and y == m - 1:
            print(visited[x][y])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visited[nx][ny] == -1 and arr[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

bfs(0, 0)
# print(visited)