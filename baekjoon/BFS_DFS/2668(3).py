from collections import defaultdict
import sys
input = sys.stdin.readline

def dfs(v, tmp):
    tmp.add(v)
    visited[v] = True

    for e in arr[v]:
        if e not in tmp:
            dfs(e, tmp.copy())
        else:
            res.extend(list(tmp))
            return


n = int(input())
arr = defaultdict(list)

for i in range(1, n + 1):
    v = int(input())
    arr[v].append(i)


res = []
visited = [False] * (n + 1)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, set([]))


res.sort()
print(len(res))
print(*res, sep="\n")
