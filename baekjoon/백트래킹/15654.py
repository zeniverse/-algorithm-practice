import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

visited = [False] * n
arr = [0] * m

def dfs(k):
    if k == m:
        print(*arr)
        return

    for i in range(len(lst)):
        if not visited[i]:
            arr[k] = lst[i]
            visited[i] = True
            dfs(k + 1)
            arr[k] = 0
            visited[i] = False

dfs(0)