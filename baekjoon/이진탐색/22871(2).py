
import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())
arr = list(map(int, input().split()))

dp = [0] + [INF] * (n - 1)

for i in range(1, n):
    for j in range(0, i):
        k = max((i - j) * (1 + abs(arr[i] - arr[j])), dp[j])
        dp[i] = min(dp[i], k)

print(dp[-1])