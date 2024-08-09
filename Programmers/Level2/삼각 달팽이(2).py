n = 4

def solution(n):
    arr = [[None] * n for _ in range(n)]
    directions = [(1, 0), (0, 1), (-1, -1)]
    num = 0
    cnt = -1
    x, y = -1, 0

    for i in range(n, 0, -1):
        cnt = cnt + 1 if cnt < 2 else 0

        for j in range(i):
            num += 1
            x = directions[cnt][0] + x
            y = directions[cnt][1] + y
            arr[x][y] = num

    return list(filter(None, sum(arr, [])))
 
print(solution(n))
        
