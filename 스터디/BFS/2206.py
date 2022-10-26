
from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs():
    visited = [[[0] * 2  for _ in range(m)] for _ in range(n)]

    queue = deque()
    queue.append((0, 0, 0))

    visited[0][0][0] = 1

    while queue:
        x, y, wall = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if arr[nx][ny] == 1 and wall == 0:
                visited[nx][ny][wall + 1] = visited[x][y][wall] + 1
                queue.append((nx, ny, wall + 1))
            
            if arr[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                visited[nx][ny][wall] = visited[x][y][wall] + 1
                queue.append((nx, ny, wall))

    return -1


print(bfs())