import sys
input = sys.stdin.readline

def dfs(color, x, y, count, start_x, start_y):
    global ans

    if ans:
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        # 사이클을 이루는지 확인
        if count >= 4 and nx == start_x and ny == start_y:
            ans = True
            return

        if visited[nx][ny] == 0 and arr[nx][ny] == color:
            visited[nx][ny] = 1
            dfs(color, nx, ny, count + 1, start_x, start_y)
            visited[nx][ny] = 0


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = False

for i in range(n):
    for j in range(m):
        start_x, start_y = i, j
        visited[start_x][start_y] = 1

        dfs(arr[i][j], i, j, 1, start_x, start_y)

        if ans:
            print('Yes')
            exit(0)
print('No')
