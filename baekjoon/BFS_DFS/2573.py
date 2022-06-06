from collections import deque
import sys
input = sys.stdin.readline


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
year = 0
flag = False


def bfs(x, y):
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if arr[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
            
            # 근접한 부분에 바다가 있다면,
            # 현재 위치인 (x, y)좌표에서 zero 리스트에 값을 추가해준다
            # (나중에 arr[x][y]에서 zero[x][y] 만큼 빼주기 위해서)
            elif arr[nx][ny] == 0:
                zero[x][y] += 1

    return 1 


while True:

    visited = [[False] * m for _ in range(n)]
    zero = [[0] * m for _ in range(n)]
    res = []

    # 빙산이 바다와 닿아있는 면적 구하기
    # res에 값을 append해서 몇개의 빙산 덩어리인지 확인 가능
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0 and not visited[i][j]:
                res.append(bfs(i, j))


    # 바다에 닿은 면적 만큼 빙산 줄이기    
    for i in range(n):
        for j in range(m):
            arr[i][j] -= zero[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0


    # 빙산이 존재하지 않는다면
    if len(res) == 0:
        print(0)
        break
    
    # 빙산이 2개이상 존재한다면
    if len(res) >= 2:
        print(year)
        break
    
    year += 1
    