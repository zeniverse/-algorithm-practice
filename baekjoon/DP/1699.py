n = int(input())

dp = [0] * 100001

for i in range(1, n + 1):
    if int(i ** 0.5) == i ** 0.5:
        dp[i] = 1
    else:
        min_ = 1e9
        for j in range(1, int(i ** 0.5) + 1):
            min_ = min(min_, dp[i - (j ** 2)])
        dp[i] = min_ + 1

print(dp[n])