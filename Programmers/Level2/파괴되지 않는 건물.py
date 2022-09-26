def solution(board, skill):
    n, m = len(board), len(board[0])
    check = [[0 for _ in range(m)] for _ in range(n)]
    res = 0

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1

        check[r1][c1] += degree
        if c2 + 1 < m:
            check[r1][c2 + 1] -= degree
        if r2 + 1 < n:
            check[r2 + 1][c1] -= degree
        if r2 + 1 < n and c2 + 1 < m:
            check[r2 + 1][c2 + 1] += degree

    for i in range(n):
        for j in range(m - 1):
            check[i][j + 1] += check[i][j]

    for j in range(m):
        for i in range(n - 1):
            check[i + 1][j] += check[i][j]

    
    for i in range(n):
        for j in range(m):
            if check[i][j] + board[i][j] > 0:
                res += 1

    return res

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

print(solution(board, skill))