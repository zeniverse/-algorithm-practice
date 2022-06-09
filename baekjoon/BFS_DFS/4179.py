from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    j_queue.append((x, y))
    visited[x][y] = 1

    while j_queue:
        queueLen = len(j_queue)

        while queueLen:
            x, y = j_queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # (r, c) 범위를 벗어나면 탈출!
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    print(visited[x][y])
                    return

                if visited[nx][ny] == 0 and arr[nx][ny] == '.':
                    visited[nx][ny] = visited[x][y] + 1
                    j_queue.append((nx, ny))

            queueLen -= 1
        
        # 지훈이가 이동을 완료했다면, 다시 불이 이동할 차례
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

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue

            if arr[nx][ny] == '.':
                arr[nx][ny] = 'F'
                f_queue.append((nx, ny))

        queueLen -= 1


r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

j_queue, f_queue = deque(), deque()
visited = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'J':
            start_x, start_y = i, j
            arr[i][j] = '.'
        
        if arr[i][j] == 'F':
            f_queue.append((i, j))

fire()
bfs(start_x, start_y)

