import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

res = []
visited = [0] * n

def dfs(idx, total):
    if idx >= 1 and total == s:
        tmp = ' '.join(map(str, visited))
        if tmp not in res:
            res.append(tmp)
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            dfs(idx + 1, total + arr[i])
            visited[i] = 0

dfs(0, 0)
print(len(res))
    
