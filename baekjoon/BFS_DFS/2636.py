from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))
    cnt = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                else:
                    # 치즈와 닿는 부분이라면, 치즈를 0으로 바꿔주기
                    visited[nx][ny] = True
                    arr[nx][ny] = 0
                    cnt += 1

    return cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
time = 0
resCheese = 0

while True:
    visited = [[False] * m for _ in range(n)]
    cheese = bfs(0, 0)

    # 더이상 녹일 치즈가 없다면
    if cheese == 0:
        break

    time += 1
    resCheese = cheese

print(time)
print(resCheese)