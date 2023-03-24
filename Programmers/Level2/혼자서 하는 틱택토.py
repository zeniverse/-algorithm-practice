
def check(p, board):
    # row
    for i in range(3):
        if all(cell == p for cell in board[i]):
            return True
        
    # column
    for i in range(3):
        if all(board[j][i] == p for j in range(3)):
            return True
    
    # diagonal
    if all(board[i][i] == p for i in range(3)):
        return True
    
    if all(board[i][2 - i] == p for i in range(3)):
        return True
    
    return False


def solution(board):
    num_x = sum(row.count('X') for row in board)
    num_o = sum(row.count('O') for row in board)

    if num_x - num_o > 0 or abs(num_x - num_o) > 1:
        return 0
    elif (check('O', board) and num_x != num_o - 1) or (check('X', board) and num_x != num_o):
        return 0
    
    return 1


board = ["O.X", ".O.", "..X"]
print(solution(board))