

m, n, board = 6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

directions = [(0, 1), (1, 0), (1, 1)]

# 4개의 블럭이 같은지 확인
def count(m, n, board, x, y, alpha):
    cnt = 0
    for x_, y_ in directions:
        if x + x_ < m and y + y_ < n:
            if board[x + x_][y + y_] == alpha and board[x + x_][y + y_] != 0:
                cnt += 1

    if cnt == 3:
        return True
    return False

# 사라진 블럭 자리로 이동
def move(m, n, board, arr):
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if arr[i][j] == 1:
                board[i][j] = 0
                for k in range(i, -1, -1):
                    if arr[k][j] == 0:
                        board[i][j] = board[k][j]
                        board[k][j] = 0
                        arr[k][j] = 1
                        break


def check(m, n, board):
    arr = [[0 for _ in range(n)] for _ in range(m)]
    flag = False

    for i in range(m):
        for j in range(n):
            if count(m, n, board, i, j, board[i][j]):
                flag = True
                arr[i][j] = 1
                for x, y in directions:
                    if i + x < m and j + y < n:
                        arr[i + x][j + y] = 1

    if flag:
        move(m, n, board, arr)

    return flag


def solution(m, n, board):
    board = [list(i) for i in board]
    res = 0
    flag = True

    while flag:
        flag = check(m, n, board)

    for i in board:
        res += i.count(0)
        
    return res

print(solution(m, n, board))