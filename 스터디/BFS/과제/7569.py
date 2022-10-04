# 2차원 배열로 해결한 토마토와 똑같이 풀었음
# 3차원이기 때문에 z축을 추가해서 리스트를 구성함
# -> for문을 돌릴때 당연하게 x축부터 돌려서 실수했음! z 축부터 돌려줘야함!

# 하루가 지나면 익은 토마토 주변의 토마토들이 익도록 변경해줘야하기 때문에
# 맨 처음 익은 토마토 위치를 queue에 기록하고, queue의 길이만큼 주변 토마토들을 익은 토마토로 변경해줬음


from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    day = -1
    
    while queue:
        day += 1

        for _ in range(len(queue)):
            z, x, y = queue.popleft()

            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
                    continue

                if arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = 1
                    queue.append((nz, nx, ny))

    for i in arr:
        for j in i:
            if 0 in j:
                return -1

    return day


m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                queue.append((i, j, k))


print(bfs())