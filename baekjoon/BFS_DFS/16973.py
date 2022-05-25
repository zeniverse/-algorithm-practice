from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
h, w, Sr, Sc, Fr, Fc = map(int, input().split())

wall = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            wall.append((i, j))

def check(i, j):
    for wall_x, wall_y in wall:
        if i <= wall_x < i + h and j <= wall_y < j + w:
            return False
    return True

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False] * m for _ in range(n)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0))

    visited[x][y] = True

    while queue:
        x, y, count = queue.popleft()

        if x == Fr - 1 and y == Fc - 1:
            return count

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if nx + h - 1 < n and ny + w - 1 < m:
                if not visited[nx][ny]:
                    if check(nx, ny):
                        visited[nx][ny] = True
                        queue.append((nx, ny, count + 1))

    return -1

print(bfs(Sr - 1, Sc - 1))
