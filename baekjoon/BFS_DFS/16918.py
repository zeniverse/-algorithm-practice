from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def plant():
    for i in range(r):
        for j in range(c):
            if arr[i][j] == '.':
                arr[i][j] = 'O'
    

def bomb():
    while queue:
        x, y = queue.popleft()

        if not visited[x][y]:
            visited[x][y] = True
            arr[x][y] = '.'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                arr[nx][ny] = '.'


r, c, n = map(int, input().split())
arr = [list(input()) for _ in range(r)]

n -= 1

while n:
    queue = deque([])

    for i in range(r):
        for j in range(c):
            if arr[i][j] == 'O':
                queue.append((i, j))
    
    plant()
    n -= 1

    if n == 0:
        break

    visited = [[False] * c for _ in range(r)]
    bomb()
    n -= 1

for i in arr:
    print("".join(i))