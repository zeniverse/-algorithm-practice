import sys
sys.setrecursionlimit(10*5)

def dfs(x, y):
    arr[x][y] = '.'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue

        if arr[nx][ny] == '#':
            dfs(nx, ny)


r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
res = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(r):
    for j in range(c):
        if arr[i][j] == '#':
            dfs(i, j)
            res += 1

print(res)
