from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    lst = []
    lst.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if l <= abs(arr[nx][ny] - arr[x][y]) <= r and not visited[nx][ny]:
                lst.append((nx, ny))
                queue.append((nx, ny))
                visited[nx][ny] = True

    return lst


def change(lst):
    num = sum([arr[x][y] for x, y in lst]) // len(lst)

    for x, y in lst:
        arr[x][y] = num


n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
count = 0

while True:
    visited = [[False] * n for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                lst = bfs(i, j)

                if len(lst) > 1:
                    flag = True
                    change(lst)

    if not flag:
        break

    count += 1

print(count)    