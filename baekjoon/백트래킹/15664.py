import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

visited = [False] * n
arr = [0] * m
res = set()

def dfs(k):
    global res
    if k == m:
        res.add(tuple(arr))
        return

    for i in range(len(lst)):
        if not visited[i]:
            if arr[k - 1] <= lst[i]:
                arr[k] = lst[i]
                visited[i] = True
                dfs(k + 1)
                arr[k] = 0
                visited[i] = False

dfs(0)
res = list(res)
res.sort()
for i in res:
    print(*i)