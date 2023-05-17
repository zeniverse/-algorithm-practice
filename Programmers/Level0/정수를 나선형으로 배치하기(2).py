# 0 : right, 1: down, 2: left, 3:up
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(n):
    board = [[0] * n for _ in range(n)]
    x, y = 0, 0
    board[0][0] = 1
    now = 2
    d = 0

    while now <= n * n:
        nx, ny = x + dx[d], y + dy[d]

        if not (0 <= nx < n and 0 <= ny < n ) or board[nx][ny]:
            d = (d + 1) % 4
            continue

        x, y = nx, ny
        board[x][y] = now
        now += 1

    return board

        
n = 4
print(solution(n))