from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(input().rstrip()) for _ in range(n)]
hx, hy = 0, 0
res = [0, 0, 0, 0, 0]


def bfs(start_x, start_y, plus_x, plus_y):
    visited = [[False] * n for _ in range(n)]

    queue = deque()
    queue.append((start_x - 1, start_y - 1))
    ans = 0

    while queue:
        x, y = queue.popleft()

        if x + plus_x < 0 or x + plus_x >= n or y + plus_y < 0 or y + plus_y >= n:
            continue

        if arr[x + plus_x][y + plus_y] == '*' and not visited[x + plus_x][y + plus_y]:
            ans += 1
            queue.append((x + plus_x, y + plus_y))

    return ans



flag = False
for i in range(n):
    for j in range(n):
        if not flag:
            if arr[i][j] == '*':
                hx = i + 2
                hy = j + 1
                flag = True
        else:
            break

res[0] = bfs(hx, hy, 0, -1)
res[1] = bfs(hx, hy, 0, 1)
res[2] = bfs(hx, hy, 1, 0)
res[3] = bfs(hx + res[2] + 1, hy - 1, 1, 0) + 1
res[4] = bfs(hx + res[2] + 1, hy + 1, 1, 0) + 1


print(hx, hy)
print(*res)