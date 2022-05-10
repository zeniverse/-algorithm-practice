from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    global count

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    arr[x][y] = count

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and arr[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                arr[nx][ny] = count


def short_bfs(num):
    global ans

    distance = [[-1] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == num:
                q.append((i, j))
                distance[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if arr[nx][ny] > 0 and arr[nx][ny] != num:
                ans = min(ans, distance[x][y])
                return

            if arr[nx][ny] == 0 and distance[nx][ny] == -1:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
count = 1
ans = sys.maxsize

for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:
            bfs(i, j)
            count += 1
            
for i in range(1, count):
    short_bfs(i)

print(ans)