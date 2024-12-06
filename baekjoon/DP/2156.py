n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

dp = [0] * (n + 1)
dp[1] = arr[1]
if n > 1:
    dp[2] =  arr[1] + arr[2]
    for i in range(3, n + 1):
        # 지금 마시지 않고 앞에서 다 마신 경우
        # 지금 마시고 + 이전에 마시고 + 이전전엔 안마신 경우(이전전전 dp합을 가져옴)
        # 지금 마시고 + 이전에 안마신 경우 (이전전 dp 합을 가져옴)
        dp[i] = max(dp[i - 1], arr[i] + arr[i - 1] + dp[i - 3], arr[i] + dp[i - 2])

print(dp[n])