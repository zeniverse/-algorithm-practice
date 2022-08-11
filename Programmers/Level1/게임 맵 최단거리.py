from collections import deque

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

n = len(maps)
m = len(maps[0])

visited = [[0] * m for _ in range(n)]

end_x = n - 1
end_y = m - 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            return visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if visited[nx][ny] == 0 and maps[nx][ny] != 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return -1

print(bfs(0, 0))






