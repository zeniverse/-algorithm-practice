dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):

    global check

    visited[x][y] = True
    check += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if not visited[nx][ny] and arr[nx][ny] ==  1:
            dfs(nx, ny)
    

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
res = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:
            check = 0
            dfs(i, j)
            res.append(check)

print(len(res))
res.sort()
for i in res:
    print(i)

            