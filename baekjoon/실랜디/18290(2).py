import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
res = -sys.maxsize

def dfs(x, y, count, sum_):
    global res
    if count == k:
        res = max(res, sum_)
        return
    
    for i in range(x, n):
        for j in range(y if x == i else 0, m):
            if visited[i][j]:
                continue

            for z in range(4):
                nx = i + dx[z]
                ny = j + dy[z]

                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:
                    break
            else:
                visited[i][j] = True
                dfs(i, j, count + 1, sum_ + arr[i][j])
                visited[i][j] = False

dfs(0, 0, 0, 0)
print(res)