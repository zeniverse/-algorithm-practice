from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    res = -1
    visited = [[False] * n for _ in range(n)]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return res

    queue = deque([(0, 0, 1)])
    visited[0][0] = True

    while queue:
        x, y, cnt = queue.popleft()

        if x == n - 1 and y == n - 1:
            res = cnt
            break

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))

    return res

gird = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(shortestPathBinaryMatrix(gird))
