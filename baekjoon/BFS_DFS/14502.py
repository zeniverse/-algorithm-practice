from collections import deque

def bfs():
    global ans

    queue = deque()

    copy_arr = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            copy_arr[i][j] = arr[i][j]
    
    for i in range(n):
        for j in range(m):
            if copy_arr[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if copy_arr[nx][ny] == 0:
                copy_arr[nx][ny] = 2
                queue.append((nx, ny))

    count = 0

    for i in range(n):
        count += copy_arr[i].count(0)
    
    ans = max(ans, count)



def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt + 1)
                arr[i][j] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

wall(0)
print(ans)


