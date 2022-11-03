import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

res = 0

def dfs(idx, total):
    global res

    if idx >= n:
        return

    total += arr[idx]

    if total == s:
        res += 1

    dfs(idx + 1, total)
    dfs(idx + 1, total - arr[idx])

dfs(0, 0)
print(res)
    
