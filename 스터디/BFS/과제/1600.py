# k번 까지만 말만큼 움직일 수 있기 때문에 k가 0이 아니라면 말처럼 움직이는 것도 진행하고 queue에 담아줘야한다.
# 하지만 k가 0이라면 상, 하, 좌, 우로만 움직여주면 된다.
# 나머지 과정은 기본 BFS와 같음!

# 주의 해야 할 것!
# 말처럼 움직일 때, 다음 좌표에서는 visited[nx][ny][k]가 아님
# 다음 좌표를 찾는 다는 것 -> 이미 1번 움직였다는 뜻
# 따라서 visited[nx][ny][k - 1] 이 방문됐는지를 확인해주면 된다.


from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
h_directions = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2) ,(-1, -2)]


def bfs():
    visited = [[[0 for _ in range(31)] for _ in range(w)] for _ in range(h)]

    queue = deque()
    queue.append((0, 0, k))

    while queue:
        x, y, z = queue.popleft()

        if x == h - 1 and y == w - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if not visited[nx][ny][z] and arr[nx][ny] != 1:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))

        if z > 0:
            for x_, y_ in h_directions:
                nx = x + x_
                ny = y + y_

                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue

                if not visited[nx][ny][z - 1] and arr[nx][ny] != 1:
                    visited[nx][ny][z - 1] = visited[x][y][z] + 1
                    queue.append((nx, ny, k - 1))

    return -1 





k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

print(bfs())
