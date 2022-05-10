import sys
sys.setrecursionlimit(100000)

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(x, y):
    visited[x][y] = True

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in direction:
        nx = x + i[0]
        ny = y + i[1]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if not visited[nx][ny] and adj[nx][ny] == 1:
            dfs(nx, ny)


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
            if adj[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1

    print(count)
