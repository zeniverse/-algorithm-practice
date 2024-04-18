n = int(input())
block = list(input())

dp = [1e9] * n
dp[0] = 0

for i in range(n):
    for j in range(i + 1, n):

        if block[i] == 'B' and block[j] == 'O':
            dp[j] = min(dp[j], dp[i] + (j - i) ** 2)
        if block[i] == 'O' and block[j] == 'J':
            dp[j] = min(dp[j], dp[i] + (j - i) ** 2)
        if block[i] == 'J' and block[j] == 'B':
            dp[j] = min(dp[j], dp[i] + (j - i) ** 2)

if dp[-1] == 1e9:
    print(-1)
else:
    print(dp[n - 1])       
