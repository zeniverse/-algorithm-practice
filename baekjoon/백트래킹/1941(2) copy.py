from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

arr = [list(input().rstrip()) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
res = 0
tmp = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def check(n):
    global visited

    x = n % 5
    y = n // 5

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
            continue

        if not visited[nx][ny]:
            if (ny * 5 + nx) in tmp:
                visited[nx][ny] = 1
                check(ny * 5 + nx)


def dfs(cnt, idx, ycnt):
    global visited, res

    if ycnt >= 4 or 25 - idx < 7 - cnt:
        return


    if cnt == 7:
        check(tmp[0])

        if sum(sum(visited, [])) == 7:
            res += 1

        visited = [[0] * 5 for _ in range(5)]
        return


    x = idx % 5
    y = idx // 5

    tmp.append(idx)

    if arr[x][y] == 'Y':
        dfs(cnt + 1, idx + 1, ycnt + 1)
    else:
        dfs(cnt + 1, idx + 1, ycnt)

    
    tmp.pop()
    dfs(cnt, idx + 1, ycnt)

dfs(0, 0, 0)
print(res)