
def solution(board, k):
    res = 0
    n = len(board)
    m = len(board[0])

    for i in range(n):
        for j in range(m):
            if i + j <= k:
                res += board[i][j]
    return res

board = [[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]]
k = 2
print(solution(board, k))