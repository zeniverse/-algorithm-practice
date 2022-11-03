import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

arr = [0] * m
res = set()

def dfs(k):
    global res
    if k == m:
        res.add(tuple(arr))
        return

    for i in range(len(lst)):
        arr[k] = lst[i]
        dfs(k + 1)
        arr[k] = 0

dfs(0)
res = list(res)
res.sort()
for i in res:
    print(*i)