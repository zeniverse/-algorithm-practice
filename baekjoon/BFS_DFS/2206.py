from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y, 0))

    visited[x][y][0] = 1

    while queue:
        x, y, wall = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽을 만났는데 한번도 벽을 부수지 않은 경우
            if arr[nx][ny] == 1 and wall == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))

            # 벽이 아니면서 방문한적 없는 경우
            elif arr[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                visited[nx][ny][wall] = visited[x][y][wall] + 1
                queue.append((nx, ny, wall))

    return -1



print(bfs(0, 0))