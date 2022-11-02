from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dh = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, 2), (-2, 1), (-1, -2), (-2, 1)]

k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

def bfs():
    visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]

    queue = deque()
    queue.append((0, 0, 0))

    while queue:
        x, y, z = queue.popleft()

        if x == h - 1 and y == w - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if visited[nx][ny][z] == 0 and arr[nx][ny] != 1:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))

        if z < k:
            for i in range(8):
                nx = x + dh[i][0]
                ny = y + dh[i][1]

                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if not visited[nx][ny][z + 1] and arr[nx][ny] != 1:
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1
                    queue.append((nx, ny, z + 1))

        

    return -1

print(bfs())