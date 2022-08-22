
def dfs(arr, n, row):
    count = 0

    if n == row:
        return 1

    for col in range(n):
        arr[row] = col

        for i in range(row):
            if arr[i] == arr[row]:
                break

            if abs(arr[i] - arr[row]) == (row - i):
                break

        else:
            count += dfs(arr, n, row + 1)

    return count
    


def solution(n):
    arr = [0] * n

    return dfs(arr, n, 0)

print(solution(4))