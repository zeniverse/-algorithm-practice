
def check(arr, o_win, x_win):
    for i in arr:
        if 'OOO' in i:
            o_win = True
        elif 'XXX' in i:
            x_win = True
    return o_win, x_win


def solution(board):
    o_count = sum([i.count('O') for i in board])
    x_count = sum([i.count('X') for i in board])

    if 0 <= o_count - x_count <= 1:
        o_win, x_win = False, False

        # 가로 빙고 확인
        o_win, x_win = check(board, o_win, x_win)

        # board 오른쪽으로 돌리기 (세로 확인을 위함)
        r_board = [board[0][i] + board[1][i] + board[2][i] for i in range(3)]
        # 세로 빙고 확인
        o_win, x_win = check(r_board, o_win, x_win)

        # 대각선
        diagonal = [board[0][0] + board[1][1] + board[2][2], board[0][2] + board[1][1] + board[2][0]]
        o_win, x_win = check(diagonal, o_win, x_win)

        # 조건 확인
        # x가 이겼는데 O도 이긴 경우
        if x_win and o_win:
            return 0
        # O가 이겼는데 O와 X의 개수가 같은 경우
        elif o_win and o_count == x_count:
            return 0
        # X가 이겼는데 O의 개수가 X보다 많은 경우 
        elif x_win and o_count > x_count:
            return 0
        else:
            return 1
    else:
        return 0


board = ["O.X", ".O.", "..X"]
print(solution(board))