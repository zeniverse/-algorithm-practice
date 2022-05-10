from collections import deque
import sys

input = sys.stdin.readline

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in direction:
            nx = x + i[0]
            ny = y + i[1]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            if adj[nx][ny] == 1:
                adj[nx][ny] = 0
                queue.append((nx, ny))


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    adj = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    count = 0

    for _ in range(k):
        y, x = map(int, input().split())
        adj[x][y] = 1

    for i in range(n):
        for j in range(m):
            if adj[i][j] == 1:
                adj[i][j] = 0
                bfs(i, j)
                count += 1

    print(count)
