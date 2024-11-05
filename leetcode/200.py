from collections import deque

def  numIslands(self, grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]
    res = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    def bfs(x, y):
        visited[x][y] = True
        queue = deque()
        queue.append((x, y))

        while queue:
            x_, y_ = queue.popleft()

            for i in range(4):
                nx = x_ + dx[i]
                ny = y_ + dy[i]

                if 0 > nx or nx >= n or ny < 0 or ny >= m:
                    continue

                if not visited[nx][ny] and grid[nx][ny] == "1":
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1" and not visited[i][j]:
                bfs(i, j)
                res += 1

    return res

