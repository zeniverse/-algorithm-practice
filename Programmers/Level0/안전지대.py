from collections import deque

board = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
directions = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]


def solution(board):
    length = len(board)
    visited = [[False] * length for _ in range(length)]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            a, b = queue.popleft()
            visited[a][b] = True

            for i in directions:
                nx = x + i[0]
                ny = y + i[1]

                if nx < 0 or nx >= length or ny < 0 or ny >= length:
                    continue

                if not visited[nx][ny]:
                    if board[nx][ny] == 1:
                        queue.append((nx, ny))
                    else:
                        board[nx][ny] = 2


    for i in range(length):
        for j in range(length):
            if board[i][j] == 1:
                bfs(i, j)

    res = 0

    for i in board:
        res += i.count(0)

    return res
    

print(solution(board))