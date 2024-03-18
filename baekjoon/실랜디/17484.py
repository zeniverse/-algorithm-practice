
max_num = int(1e9)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(m)]] + [[[max_num] * 3 for _ in range(m)] for _ in range(n)]

for i in range(1, n + 1):
    for j in range(m):
        if j < m - 1:
            dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + arr[i - 1][j]
        
        if 0 < j:
            dp[i][j][2] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][0]) + arr[i - 1][j]

        dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + arr[i - 1][j]

res = max_num

for row in dp[i]:
    for i in row:
        res = min(res, i)
        
print(res)