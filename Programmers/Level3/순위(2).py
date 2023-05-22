
def solution(n, results):
    res = 0
    arr = [[None] * n for _ in range(n)]

    for win, lose in results:
        arr[win - 1][lose - 1] = True
        arr[lose - 1][win - 1] = False

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[j][i] == arr[i][k] and arr[j][i] != None:
                    arr[j][k] = arr[j][i]
                    arr[k][j] = not arr[j][i]

    for i in range(n):
        if None in arr[i][:i] + arr[i][i + 1:]:
            continue
        res += 1
    return res

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))