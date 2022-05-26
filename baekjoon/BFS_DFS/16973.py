from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
h, w, Sr, Sc, Fr, Fc = map(int, input().split())
visited = [[False] * m for _ in range(n)]

walls = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            walls.append((i, j))

# 직사각형 안에 벽이 존재하는지 확인하기 위한 함수
def check(i, j):
    for wall_x, wall_y in walls:
        if i <= wall_x < i + h and j <= wall_y < j + w:
            return False
    return True


def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0))

    visited[x][y] = True

    while queue:
        x, y, count = queue.popleft()

        if x == Fr - 1 and y == Fc - 1:
            return count
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 직사각형의 왼쪽 상단 좌표가 주어진 좌표 크기안에 존재하는지 확인
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 직사각형이 좌표를 벗어나지 않는지 확인
            if nx + h - 1 < n and ny + w - 1 < m:
                # 직사각형의 왼쪽 상단 좌표를 방문했는지 확인
                if not visited[nx][ny]:
                    # 직사각형 크기 내의 벽이 있는지 확인
                    if check(nx, ny):
                        visited[nx][ny] = True
                        queue.append((nx, ny, count + 1))

    return -1


print(bfs(Sr - 1, Sc - 1))