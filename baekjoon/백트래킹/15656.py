import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

arr = [0] * m

def dfs(k):
    if k == m:
        print(*arr)
        return

    for i in range(len(lst)):
        arr[k] = lst[i]
        dfs(k + 1)
        arr[k] = 0

dfs(0)