from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(board):
    res = 0
    startX, startY = 0, 0
    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                startX, startY = i, j

    def bfs():
        queue = deque()
        queue.append((startX, startY))
        visited = [[0] * m for _ in range(n)]
        visited[startX][startY] = 1

        while queue:
            x, y = queue.popleft()
            if board[x][y] == 'G':
                return visited[x][y] - 1
            
            for i in range(4):
                nx, ny = x, y

                while True:
                    nx, ny = nx + dx[i], ny + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break

                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        nx -= dx[i]
                        ny -= dy[i]
                        break

                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
        return -1
    
    res = bfs()
    
    return res

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board))