from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(start_x, start_y, end_x, end_y):
    distance = [[-1] * m for _ in range(n)]

    queue = deque()
    queue.append((start_x, start_y))
    distance[start_x][start_y] = 0

    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            return distance[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if distance[nx][ny] == -1 and arr[nx][ny] != 1:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

    return float('inf')


n, m, limit_time = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            sword_x = i
            sword_y = j

# 칼 사용하지 않았을 때
timeWithoutSword = bfs(0, 0, n - 1, m - 1)

# 시작부터 칼까지의 거리
timeToSword = bfs(0, 0, sword_x, sword_y)

# sword = 시작부터 칼까지의 거리 + 칼부터 도착지점 까지의 거리
if timeToSword != float('inf'):
    sword = timeToSword + abs(n-1 - sword_x) + abs(m-1 - sword_y)
else:
    sword = timeToSword

res = min(sword, timeWithoutSword)

print(res if res <= limit_time else 'Fail')