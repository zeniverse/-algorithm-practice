from collections import deque
import sys
sys.stdin = open('input.txt')
sys.stdout = open('output.txt','w')
input = sys.stdin.readline

w, h = map(int, input().split())
arr = [[0 for _ in range(w + 2)] for _ in range(h + 2)]

for i in range(1, h + 1):
    arr[i][1:w + 1] = map(int, input().split())

dy = [0, 1, 1, 0, -1, -1]
dx = [[1, 0, -1, -1, -1, 0], [1, 1, 0, -1, 0, 1]]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))

    visited = [[False] * (w + 2) for _ in range(h + 2)]
    visited[y][x] = True
    count = 0

    while queue:
        y, x = queue.popleft()

        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[y % 2][i]

            if ny < 0 or ny >= h + 2 or nx < 0 or nx >= w + 2:
                continue

            if not visited[ny][nx] and arr[ny][nx] == 0:
                visited[ny][nx] = True
                queue.append((ny, nx))
            elif arr[ny][nx] == 1:
                count += 1

    return count

print(bfs(0, 0))

