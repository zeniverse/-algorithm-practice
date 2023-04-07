def attach(x, y, m, key, board):
    for i in range(m):
        for j in range(m):
            board[x + i][y + j] += key[i][j]

def detach(x, y, m, key, board):
    for i in range(m):
        for j in range(m):
            board[x + i][y + j] -= key[i][j]

def rotate(arr):
    return list(zip(*arr[::-1]))

def check(board, m, n):
    for i in range(n):
        for j in range(n):
            if board[m + i][m + j] != 1:
                return False
    return True


def solution(key, lock):
    m, n = len(key), len(lock)
    # 자물쇠 크기를 3배 늘리기
    new_lock = [[0] * (m * 2 + n) for _ in range(m * 2 + n)]

    # 자물쇠 중앙 배치
    for i in range(n):
        for j in range(n):
            new_lock[m + i][m + j] = lock[i][j]

    rotated_key = key

    for _ in range(4):
        rotated_key = rotate(rotated_key)
        for x in range(1, n + m):
            for y in range(1, n + m):
                attach(x, y, m, rotated_key, new_lock)
                if check(new_lock, m, n):
                    return True
                detach(x, y, m, rotated_key, new_lock)

    return False
                

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))