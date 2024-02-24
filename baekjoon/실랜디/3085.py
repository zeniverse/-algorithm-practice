n = int(input())
arr = [list(input()) for _ in range(n)]
res = 0

def check(arr):
    max_count = 1

    for i in range(n):
        count = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

        count = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

    return max_count


for i in range(n):
    for j in range(n):
        if j + 1 < n:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            count = check(arr)
            res = max(res, count)
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        
        if i + 1 < n:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            count = check(arr)
            res = max(res, count)
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(res)

