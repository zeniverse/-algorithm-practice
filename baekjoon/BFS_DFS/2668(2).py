import sys
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n + 1)]
res = []

for i in range(1, n + 1):
    adj[i].append(int(input()))


def dfs(v):
    if not visited[v]:
        visited[v] = True

        for e in adj[v]:

            first.add(v)
            second.add(e)

            if first == second:
                res.extend(first)
                return
            
            dfs(e)

    visited[v] = False



for i in range(1, n + 1):
    visited = [False] * (n + 1)
    first = set()
    second = set()

    dfs(i)

res = list(set(res))
res.sort()

print(len(res))
print(*res, sep="\n")
