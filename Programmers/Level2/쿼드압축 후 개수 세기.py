
arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]


def solution(arr):
    res = [0, 0]
    length = len(arr)

    def dfs(x, y, len):
        check = arr[x][y]

        for i in range(x, x + len):
            for j in range(y, y + len):
                if check != arr[i][j]:
                    check = -1
                    break

        if check == -1:
            len //= 2
            dfs(x, y, len)
            dfs(x, y + len, len)
            dfs(x + len, y, len)
            dfs(x + len, y + len, len)

        elif check == 0:
            res[0] += 1
        else:
            res[1] += 1

    dfs(0, 0, length)
    return res

print(solution(arr))




