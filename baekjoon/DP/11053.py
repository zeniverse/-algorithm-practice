n = int(input())
arr = list(map(int, input().split()))

# dp[i] = arr[i]를 마지막 값으로 가지는 가장 긴 증가 부분 수열의 길이
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))