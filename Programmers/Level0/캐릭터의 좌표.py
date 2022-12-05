
keyinput = ["down", "down", "down", "down", "down"]
board = [7, 9]

def solution(keyinput, board):
    dic = {"up":(0, 1), "down":(0, -1), "left":(-1, 0), "right":(1, 0)}
    x, y = 0, 0
    limit_x = board[0] // 2
    limit_y = board[1] // 2

    for i in keyinput:
        nx = x + dic[i][0]
        ny = y + dic[i][1]

        if nx < -limit_x or nx > limit_x or ny < -limit_y or ny > limit_y:
            continue

        x, y = nx, ny

    return [x, y]

print(solution(keyinput, board))
