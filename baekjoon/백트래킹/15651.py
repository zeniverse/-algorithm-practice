import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] * m

def dfs(k):
    if k == m:
        print(*arr)
        return

    for i in range(1, n + 1):
        arr[k] = i
        dfs(k + 1)
        arr[k] = 0

dfs(0)