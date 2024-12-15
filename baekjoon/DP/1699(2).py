n = int(input())

# 각 수를 1의 제곱으로만 더한게 가장 큰 횟수이기 때문에 그 수로 초기화
dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        if dp[i] > dp[i - (j ** 2)] + 1:
            dp[i] = dp[i - (j ** 2)] + 1

print(dp[n])