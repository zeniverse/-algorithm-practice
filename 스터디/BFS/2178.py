
from collections import deque


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():

    queue = deque([])
    queue.append((0, 0, 1))

    visited[0][0] = True

    while queue:
        x, y, cnt = queue.popleft()

        if x == n - 1 and y == m - 1:
            print(cnt)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))
                
bfs()