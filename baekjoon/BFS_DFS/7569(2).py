from collections import deque

dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

def bfs():
    day = -1

    while queue:
        day += 1

        for _ in range(len(queue)):
            z, x, y = queue.popleft()

            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
                    continue

                if arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = arr[z][x][y] + 1
                    queue.append((nz, nx, ny))

    for i in arr:
        for j in i:
            if 0 in j:
                return -1
        
    return day

m, n, h = map(int, input().split())
arr =[[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                queue.append((i, j, k))

print(bfs())