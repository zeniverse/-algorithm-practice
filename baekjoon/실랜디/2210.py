import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, num):
    num += arr[x][y]

    if len(num) == 6:
        res.add(num)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num)

arr = [list(input().split()) for _ in range(5)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(res))
