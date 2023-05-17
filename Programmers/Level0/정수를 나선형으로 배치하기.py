
def solution(n):
    arr = [[0] * n for _ in range(n)]

    left = 0
    right = n - 1
    up = 1
    down = n - 1

    # 0 : right, 1: down, 2: left, 3:up
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    directions = 0

    count = 1
    i = 0
    j = 0

    while count <= n * n:
        arr[i][j] = count
        count += 1

        if directions % 4 == 0 and j == right:
            directions += 1
            right -= 1
        elif directions % 4 == 1 and i == down:
            directions += 1
            down -= 1
        elif directions % 4 == 2 and j == left:
            directions += 1
            left += 1
        elif directions % 4 == 3 and i == up:
            directions += 1
            up += 1

        i += di[directions % 4]
        j += dj[directions % 4]

    return arr
        
n = 4
print(solution(n))