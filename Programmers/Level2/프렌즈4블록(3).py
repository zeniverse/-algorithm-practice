
m, n, board = 6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

def check(b, m, n):
    check_set = set()

    # 붙어있는 4개의 블럭이 있다면 check_set에 담아준다
    for i in range(n - 1):
        for j in range(m - 1):
            if b[i][j] == b[i + 1][j] == b[i][j + 1] == b[i + 1][j + 1] != '_':
                check_set |= set([(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)])

    # 블럭이 2x2가 된 부분을 0으로 변경
    for x, y in check_set:
        b[x][y] = 0
    
    # 0이된 부분 만큼 '_'로 만들고, 나머지 부분을 그대로 붙여준다
    # board를 행과 열을 변경해놨기 때문에 빈칸이 생겼을 때 블럭을 오른쪽으로 밀기 때문
    # 0 T 0 A -> _ _ T A
    for idx, row in enumerate(b):
        empty = ['_'] * row.count(0)
        b[idx] = empty + [block for block in row if block != 0]

    return len(check_set)

def solution(m, n, board):
    res = 0
    # board의 행과 열 변경 (블럭 이동을 쉽게 하기 위해서)
    board = list(map(list, zip(*board)))

    while True:
        pop = check(board, m, n)
        if pop == 0:
            return res
        res += pop


print(solution(m, n, board))