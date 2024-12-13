n = int(input())
arr = list(map(int, input().split()))
reverse_arr = arr[::-1]

dp = [1] * n
re_dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        if reverse_arr[i] > reverse_arr[j]:
            re_dp[i] = max(re_dp[i], re_dp[j] + 1)

re_dp = re_dp[::-1]
res = [0] * n
for i in range(n):
    res[i] = dp[i] + re_dp[i] - 1

print(max(res))