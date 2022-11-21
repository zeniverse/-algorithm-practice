import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

# 퇴사하기 전날부터 현재까지 이익 계산
# 만약 상담 기간이 퇴사 이후 까지라면, 현재 상담 비용 == 이후의 상담 비용
# (뒤에서부터 상담 비용을 계산했기 때문에, i일에 근무하지 않을땐 앞에서 계산한 dp[i + 1]의 비용과 같다)
# 퇴사 이전에 상담이 가능하다면, max(현재 상담을 진행했을 때, 현재 상담을 진행하지 않고 넘어갔을때)
# 현재 상담을 진행하는 경우 : 현재 상담 비용 + 상담을 끝냈을 때 날짜의 상담 비용
# 현재 상담을 진행하지 않는 경우 : 전에 계산한 상담 비용을 그대로 가져오기 때문에 dp[i + 1]
for i in range(n - 1, -1, -1):
    if i + arr[i][0] > n:
        dp[i]  = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], arr[i][1] + dp[i + arr[i][0]])

print(dp[0])