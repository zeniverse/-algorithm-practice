from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(maps):
    res = []
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)]

    def bfs(x, y):
        queue = deque([])
        queue.append((x, y))
        visited[x][y] = True
        count = int(maps[x][y])

        while queue:
            x_, y_ = queue.popleft()

            for i in range(4):
                nx = x_ + dx[i]
                ny = y_ + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    count += int(maps[nx][ny])
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        return count

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                res.append(bfs(i, j))

    if res:
        return sorted(res)
    else:
        return [-1]

maps = ["XXX","XXX","XXX"]
print(solution(maps))