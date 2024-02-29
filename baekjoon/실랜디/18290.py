
def dfs(x, y, d, s):
    global res
    if d == k:
        res = max(res, s)
        return
    else:
        for i in range(x, n):
            for j in range(y if i == x else 0, m):
                if [i, j] not in q:
                    if ([i + 1, j] not in q) and ([i - 1, j] not in q) and ([i, j + 1] not in q) and ([i, j - 1] not in q):
                        q.append([i, j])
                        dfs(i, j, d +1, s + arr[i][j])
                        q.pop()


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = []
res = -1000000
dfs(0, 0, 0, 0)
print(res)