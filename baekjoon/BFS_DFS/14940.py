from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                res[nx][ny] = res[x][y] + 1
                queue.append((nx, ny))



n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
res = [[-1] * m for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            res[i][j] = 0
        elif arr[i][j] == 2:
            queue.append((i, j))
            visited[i][j] = True
            res[i][j] = 0

bfs()

for i in res:
    print(" ".join(map(str,i)))