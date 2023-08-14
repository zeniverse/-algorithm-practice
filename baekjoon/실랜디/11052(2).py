n = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
dp[1] = cards[1]
dp[2] = max(cards[2], cards[1] * 2)

for i in range(3, n + 1):
    dp[i] = cards[i]
    for k in range(1, (i // 2) + 1):
        dp[i] = max(dp[i], dp[i - k] + dp[k])

print(dp[n])
