from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    day = -1

    while queue:

        day += 1

        for _ in range(len(queue)):
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if arr[nx][ny] == 0:
                    queue.append([nx, ny])
                    arr[nx][ny] = arr[x][y] + 1

    for i in arr:
        if 0 in i:
            return -1

    return day


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append([i, j])

print(bfs())