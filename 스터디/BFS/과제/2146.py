
# 문제를 보고 처음엔 섬들의 가장자리와 다른 섬들의 가장자리 사이의 거리를 구하려고 함.
# 가장자리를 알아내려면 좀 복잡한 과정이 필요할 것 같아서 -> 섬을 나눠서 1번 섬에서 2번 섬까지의 거리중 최소값.. 이런식으로 구하기로 결정

# 1. 섬 나누기 -> 기본 BFS를 사용해서 섬을 번호(count)로 기록해서 나눠 줬음.

# 2. 섬들 사이의 거리 중 최소값 구하기
# -> 섬의 갯수 만큼 BFS(bfs_island)를 다시 돌려서 최소값을 찾아준다.
# -> bfs_island 함수에서는 현재 num번째 섬의 좌표를 모두 queue에 담아서 동서남북 방향으로 이동해준다
# 이동하다가 바다를 만났을 때(좌포의 숫자가 0일 때)는 거리를 증가시켜주고,
# num이 아닌 다른 섬을 만났을 때는 바로 전 좌표의 거리를 res와 비교해 최소값을 기록해주면 된다.

# BFS를 두번 돌려야해서 시간 초과가 일어나지 않을까 고민했는데, 그냥 우선 해봤더니 됐다!!
# 처음 기본 BFS를 실행할때 시작점도 count로 변경해야 되는것 조심해줘야한다. 처음에 이부분 실수해서 답이 나오지 않음!


from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    global count

    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    arr[x][y] = count

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                arr[nx][ny] = count

                queue.append((nx, ny))

def bfs_island(num):
    global res

    distance = [[-1] * n for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == num:
                queue.append((i, j))
                distance[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if arr[nx][ny] > 0 and arr[nx][ny] != num:
                res = min(res, distance[x][y])
                return

            if distance[nx][ny] == -1 and arr[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
count = 1
res = sys.maxsize


for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:
            bfs(i, j)
            count += 1

for i in range(1, count):
    bfs_island(i)

print(res)