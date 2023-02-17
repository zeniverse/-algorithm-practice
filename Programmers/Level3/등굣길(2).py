from collections import deque

dx = [0, 1]
dy = [1, 0]

def solution(m, n, puddles):
    dist = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    dist[0][0] = 1
    queue = deque([(0, 0)])

    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if [ny + 1, nx + 1] in puddles:
                continue
            
            dist[nx][ny] += dist[x][y]
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return dist[n - 1][m - 1] % 1000000007
    

m = 4
n = 3
puddles = [[2, 2]]

print(solution(m, n, puddles))

