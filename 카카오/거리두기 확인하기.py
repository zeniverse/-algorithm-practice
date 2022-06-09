from collections import deque

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = []

def bfs(arr, x, y):
    visited = [[False] * 5 for _ in range(5)]

    queue = deque()
    queue.append((x, y, 0))
    visited[x][y] = True

    while queue:
        x, y, cost = queue.popleft()
        
        if cost == 2:
            continue

        for i in range(4):
            for j in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= 5 or ny <0 or ny >= 5:
                    continue

                if arr[nx][ny] == 'P' and not visited[nx][ny]:
                    return False

                if arr[nx][ny] == 'O' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cost + 1))
    return True


for place in places:
    arr = [list(place[i]) for i in range(5)]
    flag = True

    for i in range(5):
        for j in range(5):
            if arr[i][j] == 'P':
                if not bfs(arr, i, j):
                    flag = False

        if not flag:
             break

    if flag:
        res.append(1)
    else:
        res.append(0)

print(res)
