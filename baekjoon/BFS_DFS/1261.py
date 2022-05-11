from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
distance = [[-1] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()
queue.append((0, 0))
distance[0][0] = 0

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if distance[nx][ny] == -1:
            if arr[nx][ny] == 0:
                distance[nx][ny] = distance[x][y]
                queue.appendleft((nx, ny))
            else:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

print(distance[n-1][m-1])