import sys
input = sys.stdin.readline

def dfs(k):
    global n, arr, visited, res
    if k == 6:
        print(*res)
        return

    for i in range(n):
        if not visited[i]:
            if res[k - 1] < arr[i]:
                res[k] = arr[i]
                visited[i] = True
                dfs(k + 1)
                res[k] = 0
                visited[i] = False



while True:
    n, *arr = map(int, input().split())

    res = [0] * 6
    visited = [False] * n

    if n == 0:
        break

    dfs(0)
    print()
