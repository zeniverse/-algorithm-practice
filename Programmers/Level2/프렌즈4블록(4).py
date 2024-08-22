
m, n, board = 6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]

    same = set()

    while True:
        for i in range(m - 1):
            for j in range(n - 1):
                t = board[i][j]
                if t == []:
                    continue
                else:
                    if board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] == t:
                        same.add((i, j))
                        same.add((i + 1, j))
                        same.add((i, j + 1))
                        same.add((i + 1, j + 1))

        if same:
            answer += len(same)
            for i, j in same:
                board[i][j] = []
            same = set()
        else:
            break

        while True:
            flag = False
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] and board[i + 1][j] == []:
                        board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                        flage = True

            if not flag:
                break

    return answer

print(solution(m, n, board))