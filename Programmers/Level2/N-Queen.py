
def dfs(arr, n, row):
    count = 0

    if n == row:
        return 1

    for col in range(n):
        arr[row] = col

        # for-else는 break로 나오지 않았을때만 실행됨
        for i in range(row):
            # 세로로 겹치는지 확인
            if arr[i] == arr[row]:
                break

            # 대각선으로 겹치는지 확인
            if abs(arr[i] - arr[row]) == (row - i):
                break

        else:
            count += dfs(arr, n, row + 1)

    return count
    


def solution(n):
    # arr은 각 index가 row, 해당 value가 column임
    arr = [0] * n

    return dfs(arr, n, 0)

print(solution(4))