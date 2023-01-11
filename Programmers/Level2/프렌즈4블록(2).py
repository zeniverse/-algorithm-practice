from collections import deque

m, n, board = 6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

def solution(m, n, board):
    res = 0
    check_set = set()
    board = [list(i) for i in board]

    def check(b):
        for i in range(m - 1):
            for j in range(n - 1):
                if b[i][j] == b[i + 1][j] == b[i][j + 1] == b[i + 1][j + 1] != '0':
                    check_set.add((i, j))
                    check_set.add((i + 1, j))
                    check_set.add((i, j + 1))
                    check_set.add((i + 1, j + 1))

    def move(b):
        for j in range(n):
            queue = deque([])
            for i in range(m - 1, -1, -1):
                if b[i][j] == '0':
                    queue.append((i, j))
                else:
                    if queue:
                        x, y = queue.popleft()
                        b[x][y] = b[i][j]
                        b[i][j] = '0'
                        queue.append((i, j))

    while True:
        check(board)

        if check_set:
            for i, j in check_set:
                board[i][j] = '0'

            res += len(check_set)
            move(board)
            check_set.clear()
        else:
            break
        
    return res


print(solution(m, n, board))