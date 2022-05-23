from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
hx = [2, 1, -2, -1, 2, 1, -2, -1]
hy = [1, 2, -1, 2, -1, -2, 1, -2]

def bfs():
    queue = deque()
    queue.append((0, 0, k))

    # 같은 지점에서 원숭이 처럼 이동하는 방법과 말처럼 이동하는 방법 두개를 두고
    # 더 적게 이돟안 방법을 택해야하기 때문에
    # 3차원 배열을 활용해서 처리해준다.
    visited = [[[0 for _ in range(31)] for _ in range(w)] for _ in range(h)]
    
    while queue:
        x, y, z = queue.popleft()

        if x == h - 1 and y == w - 1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if visited[nx][ny][z] == 0 and arr[nx][ny] != 1:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))

        if z > 0:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]

                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                
                # 말처럼 이동해서 도착하는 지점이 visited된 적 없어야 하기 때문에
                # visited[nx][ny][z]가 아닌
                # #말처럼 이동하는 경우를 한번 뺀(현재 이동) visited[nx][ny][z - 1]을 확인해줘야한다
                if visited[nx][ny][z - 1] == 0 and arr[nx][ny] != 1:
                    visited[nx][ny][z - 1] = visited[x][y][z] + 1
                    queue.append((nx, ny, z - 1))

    return -1


k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

print(bfs())