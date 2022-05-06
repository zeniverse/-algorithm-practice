from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and arr[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                arr[nx][ny] = arr[x][y] + 1


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

bfs(0, 0)
print(arr[n - 1][m - 1])