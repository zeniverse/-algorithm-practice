from collections import deque


r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():

    while f_queue:
        x, y = f_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            
            # 방문한적 없거나, 벽이 아닌경우
            if not f_dist[nx][ny] and arr[nx][ny] != '#':
                f_dist[nx][ny] = f_dist[x][y] + 1
                f_queue.append((nx, ny))

    
    while j_queue:
        x, y = j_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                return j_dist[x][y] + 1

            # 방문한적 없거나, 벽이 아닌 경우
            if not j_dist[nx][ny] and arr[nx][ny] != '#':
                # 불이 붙은적 없거나, 불보다 지훈이가 더 빠른 경우
                if not f_dist[nx][ny] or f_dist[nx][ny] > j_dist[x][y] + 1:
                    j_dist[nx][ny] = j_dist[x][y] + 1
                    j_queue.append((nx, ny))

    return "IMPOSSIBLE"


j_queue, f_queue = deque(), deque()
j_dist = [[0] * c for _ in range(r)]
f_dist = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'J':
            j_queue.append((i, j))
        
        if arr[i][j] == 'F':
            f_queue.append((i, j))

print(bfs())

