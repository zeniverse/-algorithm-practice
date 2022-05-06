import sys
sys.setrecursionlimit(10000)

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def dfs(x, y):
    visited[x][y] = True

    for i in directions:
        nx = x + i[0]
        ny = y + i[1]

        if nx < 0 or nx >= h or ny < 0 or ny >= w:
            continue
        
        if not visited[nx][ny] and arr[nx][ny] == 1:
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and arr[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)