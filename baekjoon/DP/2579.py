n = int(input())
arr = [0]

for _ in range(n):
    arr.append(int(input()))

dp = [0] * (n + 1)
dp[1] = arr[1]

for i in range(2, n + 1):
    # i번째 계단을 2칸으로 올라온 경우, 1칸으로 올라온 경우
    dp[i] = max(dp[i - 2],  dp[i - 3] + arr[i - 1]) + arr[i]

print(dp[n])