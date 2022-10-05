
# 상근이가 있는 공간에도 불이 붙을 수 있기 때문에 우선 상근이의 위치를 기록해두고 '.'으로 변경
# 또한, 상근이는 불이 붙으려는 칸으로도 이동할 수 없기 때문에 상근이보다 불 bfs를 먼저 실행해준다.

# 1초당 불이 번지고, 상근이가 이동하기 때문에 각 queue들의 길이를 사용해서 while 문을 돌려줬음.



from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    p_queue.append((x, y))
    visited[x][y] = 1

    while p_queue:
        queueLen = len(p_queue)

        while queueLen:
            x, y = p_queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    print(visited[x][y])
                    return

                if visited[nx][ny] == 0 and arr[nx][ny] == '.':
                    visited[nx][ny] = visited[x][y] + 1
                    p_queue.append((nx, ny))

            queueLen -= 1

        fire()

    print('IMPOSSIBLE')
    return


def fire():

    queueLen = len(f_queue)

    while queueLen:
        x, y = f_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if arr[nx][ny] == '.':
                arr[nx][ny] = '*'
                f_queue.append((nx, ny))

        queueLen -= 1


for _ in range(int(input())):
    w, h = map(int, input().split())
    arr = [list(input().strip()) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    f_queue = deque()
    p_queue = deque()

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                arr[i][j] = '.'
                start_x, start_y = i, j

            if arr[i][j] == '*':
                f_queue.append((i, j))

    fire()
    bfs(start_x, start_y)